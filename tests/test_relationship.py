import mock
import responses
import unittest
import uuid
import json

from application.frontend.server import app
from application import db

from test_samples import response_json
from stub_json import response_intoduction_token_details

TITLE_NUMBER = "TN1234567"
CLIENT_LRID = uuid.UUID("f55a02a0-057b-4a3f-9e34-ede5791a5874")
TOKEN = "FKLN"
CONFIRM_RESPONSE = json.dumps({"conveyancer_name": "Tuco Salamanca"})

mock_is_matched = mock.Mock(name='is_matched')
mock_is_matched.return_value = True

class RelationshipTestCase(unittest.TestCase):

    def setUp(self):
        app.config['LOGIN_DISABLED'] = True

        db.drop_all()
        db.create_all()
        self.introductions_api = app.config['INTRODUCTION_URL']
        self.authenticated_search_api = app.config['AUTHENTICATED_SEARCH_API']
        self.matching_url = app.config['MATCHING_URL']
        self.client = app.test_client()

        with self.client.session_transaction() as sess:
            sess['lrid'] = '944ea954-01fb-4069-9010-0039929d96c8'

    def get_token_form(self):
        with app.test_request_context():
            form = {}
            form['token'] = TOKEN
            return form

    def get_confirm_form(self):
        with app.test_request_context():
            form = {}
            form['token'] = TOKEN
            form['lrid'] = CLIENT_LRID
            return form

    def get_property_form(self):
        with app.test_request_context():
            form = {}
            form['search-text'] = TITLE_NUMBER
            return form

    def get_title_form(self):
        with app.test_request_context():
            form = {}
            form['title_no'] = TITLE_NUMBER
            form['house_number'] = '111'
            form['road'] = 'High Street'
            form['town'] = 'Croydon'
            form['postalCode'] = 'CR0 1DN'
            return form

    def get_task_form(self):
        with app.test_request_context():
            form = {}
            form['buying_or_selling_property'] = 'buy'
            return form

    def get_client_form(self):
        with app.test_request_context():
            form = {}
            form['full_name'] = 'Walter White'
            form['date_of_birth'] = '01-02-1958'
            form['address'] = '1, High St, Croydon, PL1 1AA'
            form['telephone'] = '01752 210654'
            form['email'] = 'citizen@example.org'
            form['gender'] = 'M'
            return form

    def test_get_client_token_page(self):
        rv = self.client.get('/relationship/client')
        assert rv.status_code == 200

    def test_get_conveyancer_start_page(self):
        rv = self.client.get('/relationship/conveyancer')
        assert rv.status_code == 200

    def test_get_conveyancer_search_page(self):
        rv = self.client.get('/relationship/conveyancer/search')
        assert rv.status_code == 200

    @mock.patch('requests.post')
    @responses.activate
    def test_get_token_details(self, mock_post):
        responses.add(responses.GET, '%s/details/%s' % (self.introductions_api, TOKEN),
              body=response_intoduction_token_details, status=200, content_type='application/json')

        form = self.get_token_form()
        rv_post = self.client.post(
            '/relationship/client/accept',
            follow_redirects=True,
            data=DummyPostData(form))

        self.assertEquals(rv_post.status_code, 200)
        self.assertTrue('TEST1410429781566' in rv_post.data)

    @mock.patch('requests.post')
    @responses.activate
    def test_confirm_relationship(self, mock_post):
        responses.add(responses.POST, '%s/confirm' % self.introductions_api,
                      body=CONFIRM_RESPONSE, status=200, content_type='application/json')

        form = self.get_confirm_form()
        rv_post = self.client.post(
            '/relationship/client/confirm',
            follow_redirects=True,
            data=DummyPostData(form))

        self.assertEquals(rv_post.status_code, 200)
        self.assertTrue("You have confirmed" in rv_post.data)


    @responses.activate
    def test_property_search_results(self):
        responses.add(responses.GET, '%s/auth/titles/%s' % (self.authenticated_search_api, TITLE_NUMBER),
                      body=response_json, status=200, content_type='application/json')

        form = self.get_property_form()
        rv = self.client.post('/relationship/conveyancer/property',
                                    follow_redirects=True,
                                    data=DummyPostData(form))

        assert rv.status_code == 200

    @responses.activate
    def test_store_title_info_in_session(self):
        form = self.get_title_form()
        rv = self.client.post('/relationship/conveyancer/task',
                              follow_redirects=True,
                              data=DummyPostData(form))

        assert rv.status_code == 200
        with self.client.session_transaction() as sess:
            assert sess['title_no'] == TITLE_NUMBER
            assert sess['postalCode'] == 'CR0 1DN'

    @responses.activate
    def test_store_task_show_clients(self):
        form = self.get_task_form()
        rv = self.client.post('/relationship/conveyancer/client',
                              follow_redirects=True,
                              data=DummyPostData(form))

        assert rv.status_code == 200
        with self.client.session_transaction() as sess:
            assert sess['buying_or_selling'] == 'buy'

    @responses.activate
    def test_conveyancer_confirm(self):
        form = self.get_client_form()

        responses.add(responses.POST, '%s/match' % self.matching_url,
                      body=CLIENT_LRID, status=200, content_type='application/json')

        rv = self.client.post('/relationship/conveyancer/confirm',
                              follow_redirects=True,
                              data=DummyPostData(form))

        assert rv.status_code == 200


class DummyPostData(dict):
    """
    The form wants the getlist method - no problem.
    """
    def getlist(self, key):
        v = self[key]
        if not isinstance(v, (list, tuple)):
            v = [v]
        return v