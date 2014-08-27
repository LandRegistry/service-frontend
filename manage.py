import os

from flask.ext.script import Manager
from flask.ext.migrate import Migrate
from flask.ext.migrate import MigrateCommand
from werkzeug.security import generate_password_hash

from application.auth.models import *
from application import app
from application import db

app.config.from_object(os.environ['SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.option('--email', dest='email')
@manager.option('--password', dest='password')
def create_user(email, password):
    if not User.query.filter_by(email=email).first():
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()


if __name__ == '__main__':
    manager.run()
