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
    ConveyancerAddClientForm,
    ConveyancerAddClientsForm
)
from application.services import (
    post_to_cases,
    is_matched,
    is_owner,
    get_lrid_and_roles
)
from application.auth.models import User
from application import (
    app
)
from utils import get_or_log_error
from controllers import ClientController, ConveyancerController


clientController = ClientController()
conveyancerController = ConveyancerController()
search_api = app.config['SEARCH_API']


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


@app.route('/')
@login_required
def index():
    lrid, roles = get_lrid_and_roles(session)
    return render_template('index.html', roles=roles, lrid=lrid)


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

            proprietor = title['proprietors'][proprietor_index-1]
            form.proprietor_full_name.data = proprietor['full_name']

        if form.validate_on_submit():
            if 'confirm' in form and form.confirm.data:
                # the title will be persisted in its entirety when
                # it's sent to the casework system

                # HACK read title again instead of getting it from session
                title = _get_title(title_number)
                title['proprietors'][proprietor_index - 1] = {'full_name' : form.proprietor_new_full_name.data}
                form.title.data = title

                post_to_cases('change-name-marriage', form.data)
                form.title.data
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
            login_user(user, remember=form.remember.data)
            return redirect(form.next.data or url_for('.index'))
        else:
            flash("Invalid login")
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

@app.route('/relationship/client/accept/', methods=['POST'])
def client_get_relationship_details():
    url = current_app.config['INTRODUCTION_URL']+'/details/' + request.form['token']
    app.logger.info("INTRO URL: %s" % url)
    x = get_or_log_error(url)
    app.logger.info("INTRO resp: %s" % x)
    app.logger.info("INTRO resp json: %s " % x.json())
    return render_template('client-confirm.html', details = x.json(), token=request.form['token'])

@app.route('/relationship/client/confirm', methods=['POST'])
def client_confirm_relationship():
    app.logger.info('session: %s' % session['lrid'])
    request_json = json.dumps({'code':request.form['token']})
    url = current_app.config['INTRODUCTION_URL'] + '/confirm'

    app.logger.info("intro/confirm: " + url)
    response = requests.post(url, data=request_json, headers={'Content-Type': 'application/json'})

    app.logger.info("info/confirm response %s " % response.json())

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
    search_url = "%s/auth/titles/%s" % (search_api, query)
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
    return render_template('conveyancer-add-client.html',   action_path='/relationship/conveyancer/confirm', form=client_form)

@app.route('/relationship/conveyancer/confirm', methods=['POST'])
@login_required
def client_relationship_flow_step_6():
    add_client_form = ConveyancerAddClientForm(request.form)
    client_number = 1
    app.logger.debug(client_number)
    if add_client_form.validate():
        session['last_client_full_name'] = add_client_form.full_name.data
        session['last_client_date_of_birth'] = str(add_client_form.date_of_birth.data)
        session['last_client_address'] = add_client_form.address.data
        session['last_client_telephone'] = add_client_form.telephone.data
        session['last_client_email'] = add_client_form.email.data
        return render_template('conveyancer-confirm.html', dict=conveyancer_dict(),
                               client_count=num_of_clients(conveyancer_dict()), property_address=property_address())
    else:
        if client_number == 1:
            return render_template('conveyancer-add-client.html', form=add_client_form,
                                   action_path='/relationship/conveyancer/confirm', add_client_heading='add client')
        else:
            return render_template('conveyancer-add-client.html', form=add_client_form,
                                   action_path='/relationship/conveyancer/secondclient',
                                   add_client_heading='add second client')


def conveyancer_dict():

    clients = [
        {
            "lrid": "",
            "name": session['last_client_full_name'],
            "address": session['last_client_address'],
            "DOB": session['last_client_date_of_birth'],
            "tel_no": session['last_client_telephone'],
            "email": session['last_client_email']
        }
    ]

    data = {
        "conveyancer_lrid": session['lrid'],
        "title_number": session['title_no'],
        "conveyancer_name": "Da Big Boss Company",
        "conveyancer_address": "123 High Street, Stoke, ST4 4AX",
        "clients": clients,
        "task": session['buying_or_selling']
    }
    return data


def num_of_clients(conveyancer_dict):
    return len(conveyancer_dict['clients'])


def property_address():
    address = {
        "house_number": session['house_number'],
        "road": session['road'],
        "town": session['town'],
        "postalCode": session['postalCode']
    }

    return address


@app.route('/relationship/conveyancer/token')
@login_required
def conveyancer_token():
    headers = {'content-type': 'application/json'}

    data = json.dumps(conveyancer_dict())
    relationship_url = app.config['INTRODUCTION_URL'] + '/relationship'
    app.logger.debug("Sending data %s to introduction at %s" % (data, relationship_url))
    response = requests.post(relationship_url, data=data, headers=headers)
    token = response.json()['code']
    clear_captured_client_relationship_session_variables()
    return render_template('conveyancer-token.html', token=token)


def clear_captured_client_relationship_session_variables():
    session.pop('client_full_name', None)
    session.pop('client_address', None)
    session.pop('client_date_of_birth', None)
    session.pop('client_telephone', None)
    session.pop('client_email', None)
    session.pop('last_client_full_name', None)
    session.pop('last_client_address', None)
    session.pop('last_client_date_of_birth', None)
    session.pop('last_client_telephone', None)
    session.pop('last_client_email', None)
    session.pop('title_no', None)
    session.pop('buying_or_selling', None)
