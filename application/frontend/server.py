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
    ConfirmForm
)

from application.services import (
    post_to_cases,
    is_matched,
    is_owner,
    get_lrid_and_roles,
    get_client_lrid,
    is_allowed_to_see_title,
    view_count_limited
)

from application import (
    app
)

from .utils import get_or_log_error

@app.route('/')
@login_required
def index():
    lrid, roles = get_lrid_and_roles(session)
    return render_template('index.html', roles=roles, lrid=lrid)


@app.route('/property/<title_number>')
@login_required
@view_count_limited
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
           apiKey=app.config['OS_API_KEY'])


# Sticking to convention, "/property/<title_number>" will show the
# resource, and "/property/<title_number>/edit" will show a form
# to edit said resource. Here we go a step further, and limit
# the form to a section on the resource, e.g. "proprietor".
@app.route('/property/<title_number>/edit/title.proprietor.<int:proprietor_index>', methods=['GET', 'POST'])
@login_required
@view_count_limited
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

@app.route('/property/<title_number>/changes')
@login_required
@view_count_limited
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
                historical_changes_list[version['version_id']] = historian_version_response.json()['contents']['last_application']

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
@view_count_limited
def change_version(title_number, version):

    historian_version_url = app.config['HISTORIAN_URL'] + '/titles/' + title_number + '?version='
    app.logger.debug('requesting historical version from ' + historian_version_url)
    historian_version_response = requests.get(historian_version_url + version).json()['contents']
    converted_unix_timestamp = historian_version_response['last_application']
    owner = is_owner(current_user, title_number)

    return render_template(
        'view_property.html',
        historical_view='true',
        title=historian_version_response,
        is_owner=owner,
        apiKey=app.config['OS_API_KEY'],
        change_date=converted_unix_timestamp)
