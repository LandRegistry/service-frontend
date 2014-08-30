from application.frontend.server import app
from application import db
from application.auth.models import User

import requests
import responses
import mock
import unittest
import datetime

from stub_json import title
TITLE_NUMBER = "TN1234567"

class AuthenticationTestCase(unittest.TestCase):

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

    @mock.patch('requests.post')
    def test_login(self, mock_post):
        rv = self.login('landowner@mail.com', 'password')
        assert rv.status == '200 OK'

    @mock.patch('requests.post')
    def test_login_fail(self, mock_post):
         rv = self.login('********@mail.com', 'password')
         self.assertTrue('Invalid login' in rv.data)
         self.assertEqual('200 OK', rv.status)

    @mock.patch('application.auth.models.check_user_match', return_value=False)
    def test_user_with_correct_credentials_but_not_matched_rejected(self, mock_match):

        rv = self.login('landowner@mail.com', 'password')

        mock_match.assert_called_once_with(self.user)
        self.assertTrue('Invalid login' in rv.data)


    @mock.patch('requests.get')
    @mock.patch('application.auth.models.check_user_match', return_value=True)
    def test_viewing_property_requires_logged_in_and_matched_user(self, mock_match, mock_get):
        mock_get.return_value.json.return_value = title

        self.login('landowner@mail.com', 'password')
        rv = self.client.get('/property/%s' % TITLE_NUMBER)

        mock_match.assert_called_once_with(self.user)
        self.assertEquals(rv.status_code, 200)
        self.assertTrue(TITLE_NUMBER in rv.data)

    def tearDown(self):
        db.session.delete(self.user)
        db.session.commit()
