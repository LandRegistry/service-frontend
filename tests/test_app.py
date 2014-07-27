from service.server import app
from service import db
from service import user_datastore

from flask_security.utils import encrypt_password

import requests
import responses
import mock
import unittest

from test_json import response_json

TITLE_NUMBER = "TN1234567"

class ViewFullTitleTestCase(unittest.TestCase):

    def setUp(self):
        db.create_all()
        self.search_api = app.config['SEARCH_API']
        self.app = app.test_client()

        with app.test_request_context():
            user_datastore.create_user(email='landowner@mail.com',
                password=encrypt_password('password'))
            db.session.commit()


    def _login(self, email=None, password=None):
        email = email
        password = password or 'password'
        return self.app.post('/login', data={'email': email, 'password': password},
                         follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    @mock.patch('requests.get', returns=response_json)
    def test_get_property_calls_search_api(self, mock_get):

        self._login('landowner@mail.com', 'password') #need to log in in order to get to property page
        self.app.get('/property/%s' % TITLE_NUMBER)

        mock_get.assert_called_with('%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER))

    def test_login(self):
        rv = self._login('landowner@mail.com', 'password')
        assert 'No content' in rv.data
        assert rv.status == '200 OK'

    def test_login_fail(self):
        rv = self._login('********@mail.com', 'password')
        assert 'Specified user does not exist' in rv.data
        assert rv.status == '200 OK'

    # def test_logout(self):
    #   self._login('landowner@mail.com', 'password')
    #   rv = self.logout()
    #   self.app.get('/')
    #   assert 'Login' in rv.data
    #
    # def test_login_required(self):
    #   rv = self.app.get('/', follow_redirects=True)
    #   assert 'Login' in rv.data

    def test_404(self):
        rv = self.app.get('/pagedoesnotexist')
        assert rv.status == '404 NOT FOUND'

    @mock.patch('requests.get')
    @mock.patch('requests.Response')
    def test_500(self, mock_response, mock_get):

        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError

        mock_get.return_value = mock_response

        self._login('landowner@mail.com', 'password')
        response = self.app.get('/property/%s' % TITLE_NUMBER)

        assert response.status_code == 500

    @mock.patch('requests.get', side_effect=requests.exceptions.ConnectionError)
    def test_requests_connection_error_returns_500_to_client(self, mock_get):

        self._login('landowner@mail.com', 'password')
        response = self.app.get('/property/%s' % TITLE_NUMBER)

        assert response.status_code == 500


    @responses.activate
    def test_multiple_proprietors(self):
        #Mock a response, as though JSON is coming back from SEARCH_API
        responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
              body = response_json, status = 200, content_type='application/json')

        #Now call the usual Service frontend for the same title.  Redirects
        #to the mocked response in HTML.
        self._login('landowner@mail.com', 'password')
        rv = self.app.get('/property/%s' % TITLE_NUMBER, follow_redirects=True)
        assert rv.status_code == 200
        assert 'Bob Test' in rv.data
        assert 'Betty Tanker' in rv.data


    def tearDown(self):
        self.logout() #to ensure no-one is logged in after a test is run
        test_user = user_datastore.find_user(email='landowner@mail.com')
        user_datastore.delete_user(test_user)
        db.session.commit()
