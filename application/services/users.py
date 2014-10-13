from matching import check_user_match
from matching import get_client_lrid

from ownership import check_user_is_owner

from application import db
from application import app

import requests

from flask import (
    redirect,
    url_for,
    current_app
)

from flask.ext.login import (
    logout_user,
    current_user
)

from flask import session

from functools import wraps

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
        user.blocked = True
        db.session.add(user)
        db.session.commit()
        session.pop("lrid", None)
        session.pop("roles", None)
        logout_user()
        return False

def is_allowed_to_see_title(user, password):
    return not user.blocked and user.check_password(password) and is_matched(user)

def view_count_limited(func):
    '''
    This decorator must run after login_required as it
    needs to be able to get hold of current_user
    '''
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_app.config['VIEW_COUNT_ENABLED']:
            return func(*args, **kwargs)
        if is_within_view_limit(current_user):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('auth.login'))

    return decorated_view

