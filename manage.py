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
@manager.option('--name', dest='name')
@manager.option('--dob', dest='dob')
@manager.option('--gender', dest='gender')
@manager.option('--current_address', dest='current_address')
@manager.option('--previous_address', dest='previous_address')
def create_user(email, password, name, dob, gender, current_address, previous_address):
    if not User.query.filter_by(email=email).first():
        import datetime

        date_of_birth = datetime.datetime.strptime(dob, '%Y-%m-%d')

        user = User(email=email,
                    password=password,
                    name=name,
                    date_of_birth=date_of_birth,
                    gender=gender,
                    current_address=current_address,
                    previous_address=previous_address,
                    blocked=False,
                    view_count=0)

        db.session.add(user)
        db.session.commit()


@manager.command
def cleanup_expired_sessions():
    from application import app, kv_store
    kv_store.cleanup_sessions(app)

@manager.option('--email', dest='email')
def block_user(email):
    user = User.query.filter_by(email=email).first()
    if user:
        user.blocked = True

        db.session.add(user)
        db.session.commit()
        print "User %s has been blocked" % user.name
    else:
        print "User does not exist"


@manager.option('--email', dest='email')
def unblock_user(email):
    user = User.query.filter_by(email=email).first()
    if user:
        user.blocked = False

        db.session.add(user)
        db.session.commit()
        print "User %s has been unblocked" % user.name
    else:
        print "User does not exist"

@manager.command
def reset_user_view_counts():
    db.session.query(User).update({"view_count": 0})
    db.session.commit()


if __name__ == '__main__':
    manager.run()
