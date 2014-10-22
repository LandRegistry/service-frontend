import os
import logging
import redis
import urlparse

from flask import Flask
from flask import render_template
from audit import Audit
from raven.contrib.flask import Sentry

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.basicauth import BasicAuth
from flask.ext.login import LoginManager
from lrutils import dateformat, datetimeformat, currency
from health import Health

app = Flask('application.frontend')
app.config.from_object(os.environ.get('SETTINGS'))
app.jinja_env.filters['datetimeformat'] = datetimeformat
app.jinja_env.filters['dateformat'] = dateformat
app.jinja_env.filters['currency'] = currency

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)
SQLAlchemy.health = health

from flask_kvsession import KVSessionExtension
from simplekv.memory.redisstore import RedisStore

redis_url = urlparse.urlparse(app.config.get('REDIS_URL'))

redis_server = redis.StrictRedis(
        host=redis_url.hostname,
        port=redis_url.port,
        password=redis_url.password
)

store = RedisStore(redis_server)
kv_store = KVSessionExtension(store, app)

Health(app, checks=[db.health])
Audit(app)

if not app.debug:
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)

if app.config.get('BASIC_AUTH_USERNAME'):
    app.config['BASIC_AUTH_FORCE'] = True
    basic_auth = BasicAuth(app)

# Sentry exception reporting
if 'SENTRY_DSN' in os.environ:
    sentry = Sentry(app, dsn=os.environ['SENTRY_DSN'])

app.logger.debug("\nConfiguration\n%s\n" % app.config)

# import and register auth blueprint
from .auth.views import auth
app.register_blueprint(auth)
login_manager.login_view = 'auth.login'
login_manager.login_message = ''

from .relationship.views import relationship
app.register_blueprint(relationship)

def health(self):
    try:
        with self.engine.connect() as c:
            c.execute('select 1=1').fetchall()
            return True, 'DB'
    except:
        return False, 'DB'


@app.errorhandler(401)
def permission(err):
    return render_template('401.html'), 401


@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error(err):
    return render_template('500.html'), 500


@app.after_request
def after_request(response):
    # can we get some guidance on this?
    response.headers.add(
        'Content-Security-Policy',
        "default-src 'self' 'unsafe-inline' data: ; img-src *")
    response.headers.add('X-Frame-Options', 'deny')
    response.headers.add('X-Content-Type-Options', 'nosniff')
    response.headers.add('X-XSS-Protection', '1; mode=block')
    return response


@app.context_processor
def asset_path_context_processor():
    return {
        'asset_path': '/static/build/',
        'landregistry_asset_path': '/static/build/'
    }

@app.context_processor
def address_processor():
    from lrutils import build_address
    def process_address_json(address_json):
        return build_address(address_json)
    return dict(formatted=process_address_json)
