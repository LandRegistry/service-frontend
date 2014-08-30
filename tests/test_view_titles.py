from application.frontend.server import app
from application import db
from application.auth.models import User

import requests
import responses
import mock
import unittest
import datetime

from stub_json import title, response_json, response_without_charge, response_without_easement

TITLE_NUMBER = "TN1234567"

class ViewFullTitleTestCase(unittest.TestCase):

    def setUp(self):
        db.create_all()
        self.search_api = app.config['AUTHENTICATED_SEARCH_API']
        self.app = app
        self.client = app.test_client()

        self.user = User(email='landowner@mail.com',
                    password='password',
                    name='noname',
                    gender='M',
                    date_of_birth=datetime.datetime.now(),
                    current_address='nowhere',
                    previous_address='nowhere')

        db.session.add(self.user)
        db.session.commit()

    def login(self, email=None, password=None):
        email = email
        password = password or 'password'
        return self.client.post('/login', data={'email': email, 'password': password}, follow_redirects=True)

    def logout(self):
        return self.client.get('/logout', follow_redirects=True)


    @mock.patch('requests.get')
    @mock.patch('application.auth.models.check_user_match', return_value=True)
    def test_get_property_calls_search_api(self, mock_match, mock_get):
        mock_get.return_value.json.return_value = title

        self.login('landowner@mail.com', 'password')
        self.client.get('/property/%s' % TITLE_NUMBER)

        mock_get.assert_called_with('%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER))

    def test_404(self):
        rv = self.client.get('/pagedoesnotexist')
        assert rv.status == '404 NOT FOUND'

    @mock.patch('requests.get')
    @mock.patch('requests.Response')
    @mock.patch('application.auth.models.check_user_match', return_value=True)
    def test_500(self, mock_match, mock_response, mock_get):

        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError

        mock_get.return_value = mock_response

        self.login('landowner@mail.com', 'password')
        response = self.client.get('/property/%s' % TITLE_NUMBER)

        assert response.status_code == 500

    @mock.patch('requests.get', side_effect=requests.exceptions.ConnectionError)
    @mock.patch('application.auth.models.check_user_match', return_value=True)
    def test_requests_connection_error_returns_500_to_client(self, mock_match,mock_get):

        self.login('landowner@mail.com', 'password')
        response = self.client.get('/property/%s' % TITLE_NUMBER)

        assert response.status_code == 500


    @responses.activate
    @mock.patch('application.auth.models.check_user_match', return_value=True)
    def test_multiple_proprietors(self, mock_match):
        #Mock a response, as though JSON is coming back from SEARCH_API
        responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
              body = response_json, status = 200, content_type='application/json')

        #Now call the usual Service frontend for the same title.  Redirects
        #to the mocked response in HTML.
        self.login('landowner@mail.com', 'password')
        rv = self.client.get('/property/%s' % TITLE_NUMBER, follow_redirects=True)
        assert rv.status_code == 200
        assert 'Bob Test' in rv.data
        assert 'Betty Tanker' in rv.data

    @responses.activate
    @mock.patch('application.auth.models.check_user_match', return_value=True)
    def test_charges_appear(self, mock_match):
        #Mock a response, as though JSON is coming back from SEARCH_API
        responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
              body = response_json, status = 200, content_type='application/json')

        #Now call the usual Service frontend for the same title.  Redirects
        #to the mocked response in HTML.
        self.login('landowner@mail.com', 'password')
        rv = self.client.get('/property/%s' % TITLE_NUMBER, follow_redirects=True)
        assert rv.status_code == 200
        assert 'Charges Register' in rv.data
        assert 'Registered charge dated 11 August 2014.' in rv.data
        assert 'Proprietor: compone' in rv.data
        assert '(Co. Regn. No. 12345)' in rv.data
        assert 'of a warehouse.' in rv.data
        assert 'Registered charge dated 12 August 2014.' in rv.data
        assert 'Proprietor: comptwo' in rv.data
        assert '(Co. Regn. No. 56666)' in rv.data
        assert 'of a barn.' in rv.data

    @responses.activate
    @mock.patch('application.auth.models.check_user_match', return_value=True)
    def test_no_charges_header(self, mock_match):
      #Mock a response, as though JSON is coming back from SEARCH_API
      responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
            body = response_without_charge, status = 200, content_type='application/json')

      #Now call the usual Service frontend for the same title.  Redirects
      #to the mocked response in HTML.
      self.login('landowner@mail.com', 'password')
      rv = self.client.get('/property/%s' % TITLE_NUMBER, follow_redirects=True)
      assert rv.status_code == 200
      assert 'Charges Register' not in rv.data

    @responses.activate
    @mock.patch('application.auth.models.check_user_match', return_value=True)
    def test_easements_appear(self, mock_match):
        #Mock a response, as though JSON is coming back from SEARCH_API
        responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
              body = response_json, status = 200, content_type='application/json')

        #Now call the usual Service frontend for the same title.  Redirects
        #to the mocked response in HTML.
        self.login('landowner@mail.com', 'password')
        rv = self.client.get('/property/%s' % TITLE_NUMBER, follow_redirects=True)
        assert rv.status_code == 200
        assert 'Easements Register' in rv.data
        assert 'easement one' in rv.data
        assert 'easement two' in rv.data

    @responses.activate
    @mock.patch('application.auth.models.check_user_match', return_value=True)
    def test_no_easements_header(self, mock_match):
      #Mock a response, as though JSON is coming back from SEARCH_API
      responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
            body = response_without_easement, status = 200, content_type='application/json')

      #Now call the usual Service frontend for the same title.  Redirects
      #to the mocked response in HTML.
      self.login('landowner@mail.com', 'password')
      rv = self.client.get('/property/%s' % TITLE_NUMBER, follow_redirects=True)
      assert rv.status_code == 200
      assert 'Easements Register' not in rv.data

    def tearDown(self):
        db.session.delete(self.user)
        db.session.commit()

    def test_health(self):
        response = self.client.get('/health')
        assert response.status == '200 OK'
