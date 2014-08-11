import requests

from flask import render_template, request_started, request
from flask import abort
from flask.ext.login import current_user
from flask.ext.security import login_required

from service import app, db
from .health import Health
from audit import Audit
from datetime import datetime


Health(app, checks=[db.health])
Audit(app)


def get_or_log_error(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as e:
        app.logger.error("HTTP Error %s", e)
        abort(response.status_code)
    except requests.exceptions.ConnectionError as e:
        app.logger.error("Error %s", e)
        abort(500)

@app.template_filter()
def format_datetime(value):
  new_date = datetime.strptime(value,'%Y-%m-%d')
  return new_date.strftime('%d %B %Y')


@app.template_filter()
def currency(value):
    """Format a comma separated  currency to 2 decimal places."""
    return "{:,.2f}".format(float(value))


@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/property/<title_number>')
@login_required
def property_by_title(title_number):
    title_url = "%s/%s/%s" % (
        app.config['AUTHENTICATED_SEARCH_API'],
        'auth/titles',
        title_number)
    app.logger.info("Requesting title url : %s" % title_url)
    response = get_or_log_error(title_url)
    title = response.json()
    app.logger.info("Found the following title: %s" % title)
    return render_template('view_property.html', title=title)


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
        "default-src 'self' 'unsafe-inline' data:")
    response.headers.add('X-Frame-Options', 'deny')
    response.headers.add('X-Content-Type-Options', 'nosniff')
    response.headers.add('X-XSS-Protection', '1; mode=block')
    return response
