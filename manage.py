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
@manager.option('--lrid', dest='lrid')
@manager.option('--name', dest='name')
@manager.option('--dob', dest='dob')
@manager.option('--gender', dest='gender')
@manager.option('--current_address', dest='current_address')
@manager.option('--previous_address', dest='previous_address')
def create_user(email, password, lrid, name, dob, gender, current_address, previous_address):
    if not User.query.filter_by(email=email).first():
        import datetime
        import uuid
        lrid = uuid.UUID(lrid)
        user = User(email=email,
                    password=password,
                    lrid=lrid,
                    name=name,
                    date_of_birth=date_of_birth,
                    gender=gender,
                    current_address=current_address,
                    previous_address=previous_address)

        db.session.add(user)
        db.session.commit()


if __name__ == '__main__':
    manager.run()
