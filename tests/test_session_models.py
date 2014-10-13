import unittest
from application.frontend.server import app
from application.frontend import session_models
from application.frontend.forms import ConveyancerAddClientForm
from application.auth import User


class SessionModelsTestCase(unittest.TestCase):

    def setUp(self):
        app.config['LOGIN_DISABLED'] = True

        self.search_api = app.config['AUTHENTICATED_SEARCH_API']
        self.client = app.test_client()

    def test_conveyancer_dict(self):
        session = {'client_lrid':'123123', 'lrid': '456456', 'title_no': 'Title123', 'buying_or_selling':'buying'}
        expected = {'conveyancer_lrid':'456456', 'title_number': 'Title123', 'clients': [{'lrid':'123123'}], 'task':'buying'}
        self.assertEquals(expected, session_models.conveyancer_dict(session))

    def test_property_address(self):
        session = {'property_full_address': 'some address'}
        self.assertEquals(session_models.property_full_address(session), session)

    def conveyancer_form(self):
        form = ConveyancerAddClientForm()
        form.full_name.data = 'Bobby Jo'
        form.date_of_birth.data = '09-09-1980'
        form.address.data = 'some address'
        form.telephone.data = '0207090909'
        form.email.data = 'bobby.jo@gmail.com'
        form.gender.data = ('M', 'Male')
        return form

    def test_populate_client_details(self):
        with app.test_request_context():
            form = self.conveyancer_form()

            session = {}
            expected = {'client_full_name': 'Bobby Jo',
                        'client_date_of_birth':'09-09-1980',
                        'client_address':'some address',
                        'client_telephone':'0207090909',
                        'client_email':'bobby.jo@gmail.com'}

            session_models.populate_client_details(session, form)
            self.assertEquals(session, expected)

    def test_clear_captured_client_relationship_session_variables(self):
        with app.test_request_context():
            form = self.conveyancer_form()
            session = {}
            session_models.populate_client_details(session, form)
            session_models.clear_captured_client_relationship_session_variables(session)
            self.assertEquals(session, {})

    def test_create_user(self):
        with app.test_request_context():
            form = self.conveyancer_form()

            session = session_models.create_user(form)

            self.assertEquals(session, User(**{'name': form.full_name.data,
                                             'date_of_birth': form.date_of_birth.data,
                                             'current_address': form.address.data,
                                             'gender': form.gender.data
                                            }))


