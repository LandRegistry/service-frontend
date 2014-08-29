import os
import requests
from datetime import datetime

from flask import abort
from flask import render_template
from flask import request
from flask import current_app
from flask import redirect
from flask import url_for
from flask import flash

from flask.ext.login import login_user
from flask.ext.login import logout_user
from flask.ext.login import current_user
from flask.ext.login import login_required

from forms import ChangeForm
from forms import ConfirmForm
from forms import LoginForm

from application.decision import post_to_decision
from application.auth.models import User

from application import app
from application import db

@app.template_filter()
def format_date_YMD(value):
    new_date = datetime.strptime(value, '%Y-%m-%d')
    return new_date.strftime('%d %B %Y')

@app.template_filter()
def format_date_DMY(value):
    new_date = datetime.strptime(value, '%d-%m-%Y')
    return new_date.strftime('%d %B %Y')


@app.template_filter()
def currency(value):
    """Format a comma separated  currency to 2 decimal places."""
    return "{:,.2f}".format(float(value))


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

@app.route('/')
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
    return render_template(
        'view_property.html',
        title=title,
        apiKey=os.environ['OS_API_KEY'])


# Sticking to convention, "/property/<title_number>" will show the
# resource, and "/property/<title_number>/edit" will show a form
# to edit said resource. Here we go a step further, and limit
# the form to a section on the resource, e.g. "proprietor".
@app.route('/property/<title_number>/edit/title.proprietor.<int:proprietor_index>', methods=['GET', 'POST'])
@login_required
def property_by_title_edit_proprietor(title_number, proprietor_index):
    form = ChangeForm(request.form)

    if request.method == 'GET':
        title_url = "%s/%s/%s" % (
            app.config['AUTHENTICATED_SEARCH_API'],
            'auth/titles',
            title_number)
        app.logger.info("Requesting title url : %s" % title_url)
        response = get_or_log_error(title_url)
        title = response.json()
        app.logger.info("Found the following title: %s" % title)
        form.title_number.data = title['title_number']
        proprietor = title['proprietors'][proprietor_index-1]
        form.proprietor_previous_full_name.data = proprietor['full_name']

    if form.validate_on_submit():
        if 'confirm' in form and form.confirm.data:
            decision_url = '%s/decisions' % current_app.config['DECISION_URL']
            post_to_decision(decision_url, form.data)
            # TODO handle non-200 responses, and ack accordingly.
            return render_template('acknowledgement.html', form=form)
        else:
            return render_template('confirm.html', form=ConfirmForm(obj=form.data))

    return render_template('edit_property.html', form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.email.data)
        if user and user.check_password(form.password.data):
            #TODO make call to matching service
            user.authenticated = True
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=form.remember.data)
            return redirect(form.next.data)
        else:
            flash("Invalid login")
    return render_template("auth/login_user.html", form=form)


@app.route("/logout")
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('.login'))

