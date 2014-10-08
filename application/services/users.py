from matching import check_user_match
from matching import get_client_lrid

from ownership import check_user_is_owner

from application import db
from application import app

from flask.ext.login import logout_user
from flask import session

def is_matched(user):
    return check_user_match(user)

def is_owner(user, title_number):
    return check_user_is_owner(user, title_number)

def get_lrid_and_roles(session):
    return (session['lrid'], session['roles'])

def is_within_view_limit(user):
    if user.view_count < app.config['VIEW_COUNT']:
        user.view_count += 1
        db.session.add(user)
        db.session.commit()
        return True
    else:
        session.pop("lrid", None)
        session.pop("roles", None)
        logout_user()
        return False

def is_allowed_to_see_title(user, password):
    return not user.blocked and user.check_password(password) and is_matched(user)
