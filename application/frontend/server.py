import os
import requests
from datetime import datetime

from flask import abort
from flask import render_template
from flask import request
from flask import current_app
from flask.ext.security import login_required

from forms import ChangeForm
from forms import ConfirmForm
from application.decision import post_to_decision

from application import app

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
        form.proprietor_firstname.data = proprietor['first_name']
        form.proprietor_previous_surname.data = proprietor['last_name']


    if form.validate_on_submit():
        if 'confirm' in form and form.confirm.data:
            decision_url = '%s/decisions' % current_app.config['DECISION_URL']
            post_to_decision(decision_url, form.data)
            # TODO handle non-200 responses, and ack accordingly.
            return render_template('acknowledgement.html', form=form)
        else:
            return render_template('confirm.html', form=ConfirmForm(obj=form.data))


    return render_template('edit_property.html', form=form)
