import json
import requests

from flask import (
    Blueprint,
    render_template,
    flash,
    session,
    request
)

from flask.ext.login import (
    login_required,
    current_app
)

from application.frontend.utils import (
    get_or_log_error,
    build_address
)

from forms import (
    SelectTaskForm,
    ConveyancerAddClientForm
)

from application.services import (
    get_client_lrid
)

from .session_models import (
    conveyancer_dict,
    populate_client_details,
    property_full_address,
    create_user,
    clear_captured_client_relationship_session_variables
)

relationship = Blueprint('relationship', __name__, template_folder='templates' , url_prefix='/relationship')

@relationship.route('/client')
@login_required
def relationship_client():
    return render_template('client-enter-token.html')


@relationship.route('/client/accept', methods=['POST'])
@login_required
def client_get_relationship_details():
    url = current_app.config['INTRODUCTION_URL'] + '/details/' + request.form['token'].strip()
    current_app.logger.debug("INTRO URL: %s" % url)
    response = get_or_log_error(url)
    current_app.logger.debug("INTRO response json: %s " % response.json())
    return render_template('client-confirm.html', details=response.json(), token=request.form['token'].strip())


@relationship.route('/client/confirm', methods=['POST'])
@login_required
def client_confirm_relationship():
    request_json = json.dumps({'token': request.form['token'], "client_lrid": session['lrid']})
    url = current_app.config['INTRODUCTION_URL'] + '/confirm'

    response = requests.post(url, data=request_json, headers={'Content-Type': 'application/json'})

    return render_template('client-confirmed.html', conveyancer_name=response.json()['conveyancer_name'])


@relationship.route('/conveyancer')
@login_required
def conveyancer_start():
    return render_template('conveyancer-start.html')


@relationship.route('/conveyancer/search')
@login_required
def client_relationship_flow_step_1_show_search():
    return render_template('conveyancer-search.html')


@relationship.route('/conveyancer/property', methods=['POST'])
@login_required
def client_relationship_flow_step_2_render_results_in_template():
    query = request.form['search-text']
    search_url = "%s/auth/titles/%s" % ( current_app.config['AUTHENTICATED_SEARCH_API'], query)
    current_app.logger.debug("URL requested %s" % search_url)
    response = get_or_log_error(search_url)
    title = response.json()
    current_app.logger.debug("RESULT = %s" % title)
    address = build_address(title)

    return render_template('conveyancer-select-property.html',
                           title=title,
                           address=address,
                           apiKey=current_app.config['OS_API_KEY'])


@relationship.route('/conveyancer/task', methods=['POST'])
@login_required
def client_relationship_flow_step_3_store_selected_title_and_show_task_choices():
    session['title_no'] = request.form['title_no']
    session['property_full_address'] = request.form['property_full_address']
    return render_template('conveyancer-select-task.html', form=(SelectTaskForm(request.form)))


@relationship.route('/conveyancer/client', methods=['POST'])
@login_required
def client_relationship_flow_step_5a_store_number_of_clients_and_show_the_add_client_form():
    session['buying_or_selling'] = request.form['buying_or_selling_property']
    client_form = ConveyancerAddClientForm()
    return render_template('conveyancer-add-client.html', action_path='/relationship/conveyancer/confirm',
                           form=client_form)

@relationship.route('/conveyancer/confirm', methods=['POST'])
@login_required
def client_relationship_flow_step_6():
    form = ConveyancerAddClientForm(request.form)
    if form.validate_on_submit():

        populate_client_details(session, form)

        client_lrid = get_client_lrid(create_user(form))

        if client_lrid:
            session['client_lrid'] = client_lrid
        else:
            flash("The client is not in our system")
            return render_template('conveyancer-add-client.html', form=form,
                                   action_path='/relationship/conveyancer/confirm', add_client_heading='Add client')

        return render_template('conveyancer-confirm.html', dict=conveyancer_dict(session), address=property_full_address(session),
                               client_name=session['client_full_name'], client_address=session['client_address'])
    else:
        return render_template('conveyancer-add-client.html', form=form,
                               action_path='/relationship/conveyancer/confirm', add_client_heading='Add client')

@relationship.route('/conveyancer/token')
@login_required
def conveyancer_token():
    headers = {'content-type': 'application/json'}

    data = json.dumps(conveyancer_dict(session))
    relationship_url = current_app.config['INTRODUCTION_URL'] + '/relationship'

    current_app.logger.debug("Sending data %s to introduction at %s" % (data, relationship_url))
    response = requests.post(relationship_url, data=data, headers=headers)
    token = response.json()['token']
    clear_captured_client_relationship_session_variables(session)
    return render_template('conveyancer-token.html', token=token)
