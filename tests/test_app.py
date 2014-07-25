from service.server import app, db, user_datastore
from flask_security.utils import encrypt_password
from flask_security import current_user
from service.models import User
import responses
import json

import mock
import unittest

TITLE_NUMBER = "TN1234567"

class ViewProperyTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.search_api = app.config['SEARCH_API']
        SQLALCHEMY_DATABASE_URI = "sqlite://"
        app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
        db.create_all()
        self.app = app.test_client()

    def _login(self, email=None, password=None):
        email = email
        password = password or 'password'
        return self.app.post('/login', data={'email': email, 'password': password},
                         follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    @mock.patch('requests.get')
    def test_get_property_calls_search_api(self, mock_get):
        self._login('landowner@mail.com', 'password') #need to log in in order to get to property page
        self.app.get('/property/%s' % TITLE_NUMBER)
        self.assertTrue(mock_get.called)
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

    @responses.activate
    def test_multiple_proprietors(self):
      #This is the response JSON i'm mocking
      json_dict = {
          "payment": {
              "price_paid": 2000000,
              "titles": [
                  "TEST198"
              ]
          },
          "property": {
              "address": {
                  "house_number": "Flat 11 Queensmere Court",
                  "postcode": "SW13 9AT",
                  "road": "Verdun Road",
                  "town": "London"
              },
              "class_of_title": "absolute",
              "tenure": "leasehold"
          },
          "proprietors": [
              {
                  "first_name": "Bob",
                  "last_name": "Test"
              },
              {
                  "first_name": "Betty",
                  "last_name": "Tanker"
              }
          ],
          "title_number": "TEST198"
      }

      response_json = json.dumps(json_dict)

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
