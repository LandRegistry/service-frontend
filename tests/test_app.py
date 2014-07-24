from service.server import app, db, user_datastore
from flask_security.utils import encrypt_password
from flask_security import current_user
from service.models import User

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

    def test_logout(self):
      self._login('landowner@mail.com', 'password')
      rv = self.logout()
      self.app.get('/property/%s' % TITLE_NUMBER)
      assert 'Login' in rv.data
    #
    # def test_login_required(self):
    #   rv = self.app.get('/', follow_redirects=True)
    #   assert 'Login' in rv.data

    def test_404(self):
      rv = self.app.get('/pagedoesnotexist')
      assert rv.status == '404 NOT FOUND'

    def tearDown(self):
      self.logout() #to ensure no-one is logged in after a test is run
