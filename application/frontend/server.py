import os
from datetime import datetime
import json

import requests
from flask import (
    abort,
    render_template,
    request,
    current_app,
    redirect,
    url_for,
    flash,
    session
)

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
    post_to_decision,
    is_matched,
    is_owner
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
            title_url = "%s/%s/%s" % (
                app.config['AUTHENTICATED_SEARCH_API'],
                'auth/titles',
                title_number)
            app.logger.info("Requesting title url : %s" % title_url)
            response = get_or_log_error(title_url)
            title = response.json()
            app.logger.info("Found the following title: %s" % title)
            form.title_number.data = title['title_number']
            proprietor = title['proprietors'][proprietor_index - 1]
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
    else:
        abort(401)


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
    logout_user()
    return redirect(url_for('.login'))


@app.route('/relationship/client')
def relationship_client():
    return render_template(clientController.handle(session))


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
    search_api_url = "%s/%s" % (search_api, 'search')
    search_url = "%s?query=%s" % (search_api_url, query)
    app.logger.info("URL requested %s" % search_url)
    response = get_or_log_error(search_url)
    result_json = response.json()
    app.logger.info("Found for the following %s result: %s"
                    % (len(result_json['results']), result_json))

    return render_template('conveyancer-select-property.html',
                           results=result_json['results'],
                           apiKey=os.environ['OS_API_KEY'])


@app.route('/relationship/conveyancer/task', methods=['POST'])
@login_required
def client_relationship_flow_step_3_store_selected_title_and_show_task_choices():
    session['title_no'] = request.form['title_no']
    return render_template('conveyancer-select-task.html', form=(SelectTaskForm(request.form)))


@app.route('/relationship/conveyancer/clients', methods=['POST'])
@login_required
def client_relationship_flow_step_4_store_task_choices_and_render_number_of_clients_form():
    form = SelectTaskForm(request.form)
    session['buying_or_selling'] = form.buying_or_selling_property.data
    session['another_task'] = form.another_task.data
    return render_template('conveyancer-add-clients.html', form=(ConveyancerAddClientsForm(request.form)))


@app.route('/relationship/conveyancer/client', methods=['POST'])
@login_required
def client_relationship_flow_step_5a_store_number_of_clients_and_show_the_add_client_form():
    number_of_clients_form = ConveyancerAddClientsForm(request.form)
    session['number_of_clients'] = number_of_clients_form.num_of_clients.data
    if number_of_clients_form.num_of_clients.data == '1':
        return render_template('conveyancer-add-client.html', add_client_heading='add client',
                               action_path='/relationship/conveyancer/confirm',
                               form=(ConveyancerAddClientForm(request.form)))
    else:
        return render_template('conveyancer-add-client.html', add_client_heading='add first client',
                               action_path='/relationship/conveyancer/secondclient',
                               form=(ConveyancerAddClientForm(request.form)))


@app.route('/relationship/conveyancer/secondclient', methods=['POST'])
@login_required
def client_relationship_flow_step_5b_show_the_add_second_client_form():
    return render_template('conveyancer-add-client.html', add_client_heading='add second client',
                           action_path='/relationship/conveyancer/confirm',
                           form=(ConveyancerAddClientForm(request.form)))


@app.route('/relationship/conveyancer/confirm', methods=['POST'])
@login_required
def client_relationship_flow_step_6():
    return render_template('conveyancer-confirm.html')


@app.route('/relationship/conveyancer/token')
@login_required
def conveyancer_token():
    headers = {'content-type': 'application/json'}
    test_json = json.dumps({"conveyancer_lrid": "9c0250cd-dba7-4f7e-b7f5-5d526815bd28", "title_number": "DN100",
                            "clients": ["b5fafd71-0c60-4a54-b7d0-bedcc8de358c",
                                        "fc3b9a32-5887-46e7-9885-c9dd30681f30"]})
    relationship_url = app.config['INTRODUCTION_URL'] + '/relationship'
    app.logger.info("Sending data %s to introduction at %s" % (test_json, relationship_url))
    response = requests.post(relationship_url, data=test_json, headers=headers)
    token = response.json()['code']
    return render_template('conveyancer-token.html', token=token)
