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
    current_app
)
from flask.ext.login import (
    login_required,
    current_user
)
from forms import (
    ChangeForm,
    ConfirmForm,
    SelectTaskForm,
    ConveyancerAddClientForm
)
from application.services import (
    post_to_cases,
    is_matched,
    is_owner,
    get_lrid_and_roles,
    get_client_lrid,
    is_within_view_limit,
    is_allowed_to_see_title
)
from application.auth.models import User
from application import (
    app
)
from utils import (
    get_or_log_error,
    build_address
)

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

@app.template_filter()
def format_date_time_iso_8601(value):
    split_date_by_microseconds = value.split(".")
    DMYHMS = split_date_by_microseconds[0]
    new_datetime = datetime.strptime(DMYHMS, '%Y-%m-%d %H:%M:%S')
    return _tz(new_datetime).strftime('%Y-%m-%d %H:%M')

def unix_timestamp_to_DMYHMS(value):
    return datetime.fromtimestamp(int(value)).strftime('%d %B %Y %H:%M:%S')


@app.route('/')
@login_required
def index():
    lrid, roles = get_lrid_and_roles(session)
    return render_template('index.html', roles=roles, lrid=lrid)


@app.route('/property/<title_number>')
@login_required
def property_by_title(title_number):
    if is_within_view_limit(current_user):
        title_url = "%s/%s/%s" % (
           app.config['AUTHENTICATED_SEARCH_API'],
           'auth/titles',
           title_number)
        app.logger.debug("Requesting title url : %s" % title_url)
        response = get_or_log_error(title_url)
        title = response.json()

        app.logger.debug("Found the following title: %s" % title)
        owner = is_owner(current_user, title_number)
        address = build_address(title)

        return render_template(
           'view_property.html',
           title=title,
           is_owner=owner,
           address=address,
           apiKey=app.config['OS_API_KEY'])
    else:
        return redirect(url_for('auth.login'))


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

            proprietor = title['proprietorship']['fields']['proprietors'][proprietor_index - 1]
            form.proprietor_full_name.data = proprietor['name']['full_name']

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


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.get(form.email.data)
#         if user and is_allowed_to_see_title(user, form.password.data):
#             login_user(user)
#             return redirect(form.next.data or url_for('.index'))
#         else:
#             app.logger.info("Login failed for user email %s" % form.email.data)
#             flash("Sorry, those details haven&rsquo;t been recognised. Please try again.")
#     return render_template("auth/login_user.html", form=form)


# @app.route("/logout")
# @login_required
# def logout():
#     session.pop("lrid", None)
#     session.pop("roles", None)
#     logout_user()
#     return redirect(url_for('.login'))


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
    title = response.json()
    app.logger.debug("RESULT = %s" % title)
    address = build_address(title)

    return render_template('conveyancer-select-property.html',
                           title=title,
                           address=address,
                           apiKey=app.config['OS_API_KEY'])


@app.route('/relationship/conveyancer/task', methods=['POST'])
@login_required
def client_relationship_flow_step_3_store_selected_title_and_show_task_choices():
    session['title_no'] = request.form['title_no']
    session['property_full_address'] = request.form['property_full_address']
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

        return render_template('conveyancer-confirm.html', dict=conveyancer_dict(), address=property_full_address(),
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


def property_full_address():
    address = {
        "property_full_address": session['property_full_address'],
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
    session.pop('property_full_address', None)


@app.route('/property/<title_number>/changes')
@login_required
def changes(title_number):
    if is_owner(current_user, title_number):
        cases_url = app.config['CASES_URL'] + '/cases/property/' + title_number
        app.logger.debug("Requesting cases from %s" % cases_url)
        cases_response = requests.get(cases_url)
        cases = cases_response.json()
        pending = []
        historical_changes_list = {}

        historian_list_url = app.config['HISTORIAN_URL'] + '/titles/' + title_number + '?version=list'
        historian_version_url = app.config['HISTORIAN_URL'] + '/titles/' + title_number + '?version='
        app.logger.debug('requesting history from ' + historian_list_url)
        historian_list_response = requests.get(historian_list_url)
        if historian_list_response:
            #version information put in a list to pass to the template.
            for version in historian_list_response.json()['versions']:
                historian_version_response = requests.get(historian_version_url + version['version_id'])
                historical_changes_list[version['version_id']] = historian_version_response.json()['contents']['edition_date']

        for case in cases:
            if case['status'] != 'completed':
                pending.append(case)

        order_by_latest_version_first = list(reversed(sorted(historical_changes_list.keys())))

        return render_template('changes.html', title_number=title_number, pending=pending,
                               historical_changes=historical_changes_list,
                               order_by_latest_version_first=order_by_latest_version_first)
    else:
        abort(401)

@app.route('/property/<title_number>/changes/<version>')
@login_required
def change_version(title_number, version):

    historian_version_url = app.config['HISTORIAN_URL'] + '/titles/' + title_number + '?version='
    app.logger.debug('requesting historical version from ' + historian_version_url)
    historian_version_response = requests.get(historian_version_url + version).json()['contents']
    converted_unix_timestamp = historian_version_response['edition_date']
    owner = is_owner(current_user, title_number)
    address = build_address(title)

    return render_template(
        'view_property.html',
        historical_view='true',
        title=historian_version_response,
        address=address,
        is_owner=owner,
        apiKey=app.config['OS_API_KEY'],
        change_date=converted_unix_timestamp)


