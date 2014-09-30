import os
from datetime import datetime
import json

import requests
from flask import (
    abort,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
    current_app)

from flask.ext.login import (
    login_user,
    logout_user,
    login_required,
    current_user
)
from forms import (
    ChangeForm,
    ConfirmForm,
    LoginForm,
    SelectTaskForm,
    ConveyancerAddClientForm
)
from application.services import (
    post_to_cases,
    is_matched,
    is_owner,
    get_lrid_and_roles,
    get_client_lrid
)
from application.auth.models import User
from application import (
    app
)
from utils import get_or_log_error

from pytz import timezone


@app.template_filter()
def format_date_YMD(value):
    new_date = datetime.strptime(value, '%Y-%m-%d')
    return new_date.strftime('%d %B %Y')


@app.template_filter()
def format_date_DMY(value):
    new_date = datetime.strptime(value, '%d-%m-%Y')
    return new_date.strftime('%d %B %Y')

def _tz(dt):
    utc = timezone('UTC').localize(dt)
    bst = timezone('Europe/London').localize(dt)
    return bst + (utc - bst)

@app.template_filter()
def format_date_time_DMYHM(value):
    new_datetime = datetime.strptime(value, '%d-%m-%Y %H:%M:%S')
    return _tz(new_datetime).strftime('%d-%m-%Y %H:%M')

@app.template_filter()
def currency(value):
    """Format a comma separated  currency to 2 decimal places."""
    return "{:,.2f}".format(float(value))


@app.route('/')
@login_required
def index():
    lrid, roles = get_lrid_and_roles(session)
    return render_template('index.html', roles=roles, lrid=lrid)


# TEMP - sketched in Register View
@app.route('/property/register')
@login_required
def view_register():
    lrid, roles = get_lrid_and_roles(session)
    return render_template('view_register.html', roles=roles, lrid=lrid)


@app.route('/property/<title_number>')
@login_required
def property_by_title(title_number):
    title_url = "%s/%s/%s" % (
        app.config['AUTHENTICATED_SEARCH_API'],
        'auth/titles',
        title_number)
    app.logger.debug("Requesting title url : %s" % title_url)
    response = get_or_log_error(title_url)
    title = response.json()
    app.logger.debug("Found the following title: %s" % title)
    owner = is_owner(current_user, title_number)
    return render_template(
        'view_property.html',
        title=title,
        is_owner=owner,
        apiKey=os.environ['OS_API_KEY'])


# Sticking to convention, "/property/<title_number>" will show the
# resource, and "/property/<title_number>/edit" will show a form
# to edit said resource. Here we go a step further, and limit
# the form to a section on the resource, e.g. "proprietor".
@app.route('/property/<title_number>/edit/title.proprietor.<int:proprietor_index>', methods=['GET', 'POST'])
@login_required
def property_by_title_edit_proprietor(title_number, proprietor_index):
    if is_owner(current_user, title_number):
        form = ChangeForm(request.form, marriage_country='GB')
        if request.method == 'GET':
            title = _get_title(title_number)
            app.logger.debug("Found the following title: %s" % title)
            form.title_number.data = title['title_number']

            proprietor = title['proprietors'][proprietor_index - 1]
            form.proprietor_full_name.data = proprietor['full_name']

        if form.validate_on_submit():
            if 'confirm' in form and form.confirm.data:

                post_to_cases('change-name-marriage', form.data)
                # TODO handle non-200 responses, and ack accordingly.
                return render_template('acknowledgement.html', form=form)
            else:
                from datatypes.validators.iso_country_code_validator import countries

                country = countries.get(alpha2=form.data['marriage_country']).name
                return render_template('confirm.html', form=ConfirmForm(obj=form.data), country=country)
        return render_template('edit_property.html', form=form)
    else:
        abort(401)


def _get_title(title_number):
    title_url = "%s/%s/%s" % (
        app.config['AUTHENTICATED_SEARCH_API'],
        'auth/titles',
        title_number)
    app.logger.debug("Requesting title url : %s" % title_url)
    response = get_or_log_error(title_url)
    return response.json()


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.email.data)
        if user and user.check_password(form.password.data) and is_matched(user):
            login_user(user)
            return redirect(form.next.data or url_for('.index'))
        else:
            flash("Sorry, those details haven&rsquo;t been recognised. Please try again.")
    return render_template("auth/login_user.html", form=form)


@app.route("/logout")
@login_required
def logout():
    session.pop("lrid", None)
    session.pop("roles", None)
    logout_user()
    return redirect(url_for('.login'))


@app.route('/relationship/client')
def relationship_client():
    return render_template('client-enter-token.html')


@app.route('/relationship/client/accept', methods=['POST'])
def client_get_relationship_details():
    url = current_app.config['INTRODUCTION_URL'] + '/details/' + request.form['token']
    app.logger.debug("INTRO URL: %s" % url)
    response = get_or_log_error(url)
    app.logger.debug("INTRO response json: %s " % response.json())
    return render_template('client-confirm.html', details=response.json(), token=request.form['token'])


@app.route('/relationship/client/confirm', methods=['POST'])
def client_confirm_relationship():
    request_json = json.dumps({'token': request.form['token'], "client_lrid": session['lrid']})
    url = current_app.config['INTRODUCTION_URL'] + '/confirm'

    response = requests.post(url, data=request_json, headers={'Content-Type': 'application/json'})

    return render_template('client-confirmed.html', conveyancer_name=response.json()['conveyancer_name'])


@app.route('/relationship/conveyancer')
def conveyancer_start():
    return render_template('conveyancer-start.html')


@app.route('/relationship/conveyancer/search')
@login_required
def client_relationship_flow_step_1_show_search():
    return render_template('conveyancer-search.html')


@app.route('/relationship/conveyancer/property', methods=['POST'])
@login_required
def client_relationship_flow_step_2_render_results_in_template():
    query = request.form['search-text']
    search_url = "%s/auth/titles/%s" % ( app.config['AUTHENTICATED_SEARCH_API'], query)
    app.logger.debug("URL requested %s" % search_url)
    response = get_or_log_error(search_url)
    result_json = response.json()
    app.logger.debug("RESULT = %s" % result_json)
    return render_template('conveyancer-select-property.html',
                           title=result_json,
                           apiKey=os.environ['OS_API_KEY'])


@app.route('/relationship/conveyancer/task', methods=['POST'])
@login_required
def client_relationship_flow_step_3_store_selected_title_and_show_task_choices():
    session['title_no'] = request.form['title_no']
    session['house_number'] = request.form['house_number']
    session['road'] = request.form['road']
    session['town'] = request.form['town']
    session['postalCode'] = request.form['postalCode']
    return render_template('conveyancer-select-task.html', form=(SelectTaskForm(request.form)))


@app.route('/relationship/conveyancer/client', methods=['POST'])
@login_required
def client_relationship_flow_step_5a_store_number_of_clients_and_show_the_add_client_form():
    session['buying_or_selling'] = request.form['buying_or_selling_property']
    client_form = ConveyancerAddClientForm()
    return render_template('conveyancer-add-client.html', action_path='/relationship/conveyancer/confirm',
                           form=client_form)


@app.route('/relationship/conveyancer/confirm', methods=['POST'])
@login_required
def client_relationship_flow_step_6():
    form = ConveyancerAddClientForm(request.form)
    if form.validate_on_submit():

        session['client_full_name'] = form.full_name.data
        session['client_date_of_birth'] = str(form.date_of_birth.data)
        session['client_address'] = form.address.data
        session['client_telephone'] = form.telephone.data
        session['client_email'] = form.email.data

        client_lrid = get_client_lrid(_create_user(form))

        if client_lrid:
            session['client_lrid'] = client_lrid
        else:
            flash("The client is not in our system")
            return render_template('conveyancer-add-client.html', form=form,
                                   action_path='/relationship/conveyancer/confirm', add_client_heading='Add client')

        return render_template('conveyancer-confirm.html', dict=conveyancer_dict(), property_address=property_address(),
                               client_name=session['client_full_name'], client_address=session['client_address'])
    else:
        return render_template('conveyancer-add-client.html', form=form,
                               action_path='/relationship/conveyancer/confirm', add_client_heading='Add client')


def conveyancer_dict():
    client = [{
                  "lrid": session['client_lrid']
              }]

    data = {
        "conveyancer_lrid": session['lrid'],
        "title_number": session['title_no'],
        "clients": client,
        "task": session['buying_or_selling']
    }

    return data


def property_address():
    address = {
        "house_number": session['house_number'],
        "road": session['road'],
        "town": session['town'],
        "postalCode": session['postalCode']
    }

    return address


def _create_user(form):
    client_data = {'name': form.full_name.data,
                   'date_of_birth': form.date_of_birth.data,
                   'current_address': form.address.data,
                   'gender': form.gender.data}
    return User(**client_data)


@app.route('/relationship/conveyancer/token')
@login_required
def conveyancer_token():
    headers = {'content-type': 'application/json'}

    data = json.dumps(conveyancer_dict())
    relationship_url = app.config['INTRODUCTION_URL'] + '/relationship'

    app.logger.debug("Sending data %s to introduction at %s" % (data, relationship_url))
    response = requests.post(relationship_url, data=data, headers=headers)
    token = response.json()['token']
    clear_captured_client_relationship_session_variables()
    return render_template('conveyancer-token.html', token=token)


def clear_captured_client_relationship_session_variables():
    session.pop('client_full_name', None)
    session.pop('client_address', None)
    session.pop('client_date_of_birth', None)
    session.pop('client_telephone', None)
    session.pop('client_lrid', None)
    session.pop('title_no', None)
    session.pop('buying_or_selling', None)


@app.route('/property/<title_number>/changes')
@login_required
def changes(title_number):
    if is_owner(current_user, title_number):
        cases_url = app.config['CASES_URL'] + '/cases/property/' + title_number
        app.logger.debug("Requesting cases from %s" % cases_url)
        response = requests.get(cases_url)
        cases = response.json()
        pending = []
        previous = []
        for case in cases:
            if case['status'] != 'completed':
                pending.append(case)
            else:
                previous.append(case)
        app.logger.debug("Received cases from %s: %s" % (cases_url, cases))
        return render_template('changes.html', title_number=title_number, pending=pending, previous=previous)
    else:
        abort(401)
