from service.server import app, db, user_datastore
from flask_security.utils import encrypt_password
from service.models import User

import mock
import unittest

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
        self._login('landowner@mail.com', 'password')
        title_number = "TN1234567"
        self.app.get('/property/%s' % title_number)
        self.assertTrue(mock_get.called)
        mock_get.assert_called_with('%s/auth/titles/%s' % (self.search_api, title_number))
