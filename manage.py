import os

from flask.ext.script import Manager
from flask.ext.script import Command
from flask.ext.migrate import Migrate
from flask.ext.migrate import MigrateCommand
from flask_security.utils import encrypt_password

from service.models import *
from service import app
from service import db
from service import user_datastore


app.config.from_object(os.environ['SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.option('-e', '--email', dest='email')
@manager.option('-p', '--password', dest='password')
def create_user(email, password):
    if not user_datastore.find_user(email=email):
        user_datastore.create_user(email=email,
            password=encrypt_password(password))
        db.session.commit()


if __name__ == '__main__':
    manager.run()
