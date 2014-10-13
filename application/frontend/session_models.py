from application.auth import User


def conveyancer_dict(session):
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


def property_full_address(session):
    address = {
        "property_full_address": session['property_full_address'],
        }
    return address

def populate_client_details(session, form):
    session['client_full_name'] = form.full_name.data
    print form.full_name.data
    session['client_date_of_birth'] = str(form.date_of_birth.data)
    session['client_address'] = form.address.data
    session['client_telephone'] = form.telephone.data
    session['client_email'] = form.email.data

def create_user(form):
    client_data = {'name': form.full_name.data,
                   'date_of_birth': form.date_of_birth.data,
                   'current_address': form.address.data,
                   'gender': form.gender.data}
    return User(**client_data)

def clear_captured_client_relationship_session_variables(session):
    session.pop('client_full_name', None)
    session.pop('client_address', None)
    session.pop('client_date_of_birth', None)
    session.pop('client_telephone', None)
    session.pop('client_lrid', None)
    session.pop('title_no', None)
    session.pop('buying_or_selling', None)
    session.pop('property_full_address', None)
    session.pop('client_email')