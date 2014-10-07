from application.frontend.server import app
from application import db
from application.auth.models import User

import requests
import responses
import mock
import unittest
import datetime
import uuid

from test_samples import title, response_json
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
                    previous_address='nowhere',
                    blocked=False,
                    view_count=0)

        self.blocked_user = User(email='landowner2@mail.com',
                     password='password',
                     name='noname',
                     gender='M',
                     date_of_birth=datetime.datetime.now(),
                     current_address='nowhere',
                     previous_address='nowhere',
                     blocked=True,
                     view_count=0)

        db.session.add(self.user)
        db.session.add(self.blocked_user)
        db.session.commit()

        self.lrid = uuid.uuid4()
        self.roles = ['CITIZEN']

    def login(self, email=None, password=None):
        password = password or 'password'
        return self.client.post('/login', data={'email': email, 'password': password}, follow_redirects=True)

    def logout(self):
        return self.client.get('/logout', follow_redirects=True)

    @mock.patch('requests.post')
    def test_login(self, mock_post):
        mock_post.return_value.json.return_value = {"lrid":self.lrid, "roles":self.roles}
        rv = self.login('landowner@mail.com', 'password')
        assert rv.status == '200 OK'

    @mock.patch('requests.post')
    def test_blocked_login(self, mock_post):
        self.logout()
        mock_post.return_value.json.return_value = {"lrid":self.lrid, "roles":self.roles}
        rv = self.login('landowner2@mail.com', 'password')
        assert rv.status == '200 OK'
        self.assertTrue('Sorry, those details haven&rsquo;t been recognised. Please try again.' in rv.data)

    @mock.patch('requests.post')
    @mock.patch('application.frontend.server.is_matched', return_value=True)
    def test_login_fail(self, mock_check, mock_post):
         rv = self.login('********@mail.com', 'password')
         self.assertTrue('Sorry, those details haven&rsquo;t been recognised. Please try again.' in rv.data)
         self.assertEqual('200 OK', rv.status)

    @mock.patch('application.frontend.server.is_matched', return_value=False)
    def test_user_with_correct_credentials_but_not_matched_rejected(self, mock_check):

        rv = self.login('landowner@mail.com', 'password')

        mock_check.assert_called_once()
        self.assertTrue('Sorry, those details haven&rsquo;t been recognised. Please try again.' in rv.data)


    @mock.patch('requests.get')
    @mock.patch('requests.post')
    @mock.patch('application.frontend.server.is_owner', return_value=False)
    def test_viewing_property_requires_logged_in_and_matched_user(self, mock_owner, mock_post, mock_get):
        mock_post.return_value.json.return_value = {"lrid":self.lrid, "roles":self.roles}
        mock_get.return_value.json.return_value = title

        self.login('landowner@mail.com', 'password')
        rv = self.client.get('/property/%s' % TITLE_NUMBER)

        mock_owner.assert_called_once()
        self.assertEquals(rv.status_code, 200)
        self.assertTrue(TITLE_NUMBER in rv.data)


    @mock.patch('requests.get')
    @mock.patch('requests.post')
    @mock.patch('application.frontend.server.is_owner', return_value=False)
    def test_view_changes_requires_logged_in_and_owner_user(self, mock_owner, mock_post, mock_get):
        mock_post.return_value.json.return_value = {"lrid":self.lrid, "roles":self.roles}
        mock_get.return_value.json.return_value = title

        self.login('landowner@mail.com', 'password')
        rv = self.client.get('/property/%s/changes' % TITLE_NUMBER)

        mock_owner.assert_called_once()
        self.assertEquals(rv.status_code, 401)


    def tearDown(self):
        db.session.delete(self.user)
        db.session.delete(self.blocked_user)
        db.session.commit()
