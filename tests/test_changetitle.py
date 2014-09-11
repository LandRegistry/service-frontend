from application.frontend.server import app
from application import db
from application.auth.models import User

import mock
import responses
import unittest
import datetime

from stub_json import response_json

TITLE_NUMBER = "TN1234567"

class ChangeTitleTestCase(unittest.TestCase):

    def setUp(self):
        db.drop_all()
        db.create_all()
        self.search_api = app.config['AUTHENTICATED_SEARCH_API']
        self.client = app.test_client()

        user = User(email='landowner@mail.com',
                    password='password',
                    name='noname',
                    gender='M',
                    date_of_birth=datetime.datetime.now(),
                    current_address='nowhere',
                    previous_address='nowhere')

        db.session.add(user)
        db.session.commit()


    def _login(self, email=None, password=None):
        email = email
        password = password or 'password'
        return self.client.post('/login', data={'email': email, 'password': password}, follow_redirects=True)

    def logout(self):
        return self.client.get('/logout', follow_redirects=True)


    def get_unconfirmed_change_form(self):
        with app.test_request_context():
            form = {}
            form['title_number'] = TITLE_NUMBER
            form['proprietor_full_name'] = 'Proprietor Previous Full Name'
            form['proprietor_new_full_name'] = 'Proprietor New full name'
            form['partner_name'] = 'Partner Name'
            form['marriage_date'] = '01-01-2014'
            form['marriage_place'] = 'Testville'
            form['marriage_country'] = 'GB'
            form['marriage_certificate_number'] = '00000000'
            return form


    @mock.patch('application.frontend.server.is_matched', return_value=True)
    @mock.patch('application.frontend.server.is_owner', return_value=True)
    @mock.patch('requests.post')
    @responses.activate
    def test_owner_can_change_register(self, mock_user_match, mock_owner_check, mock_post):
        #Mock a response, as though JSON is coming back from SEARCH_API
        responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
              body = response_json, status = 200, content_type='application/json')

        # load the form

        self._login('landowner@mail.com', 'password')
        rv = self.client.get('/property/%s/edit/title.proprietor.1' % TITLE_NUMBER, follow_redirects=True)
        self.assertEquals(rv.status_code, 200)

        self.assertTrue('Change register' in rv.data)

        # post the change

        form = self.get_unconfirmed_change_form()
        rv_post = self.client.post(
            '/property/%s/edit/title.proprietor.1' % TITLE_NUMBER,
            follow_redirects=True,
            data=DummyPostData(form))
        self.assertEquals(rv_post.status_code, 200)
        self.assertTrue('I confirm that I' in rv_post.data)

        # # confirm

        form['confirm'] = True
        rv_post_confirm = self.client.post(
            '/property/%s/edit/title.proprietor.1' % TITLE_NUMBER,
            follow_redirects=True,
            data=DummyPostData(form))
        self.assertEquals(rv_post_confirm.status_code, 200)
        self.assertTrue('Application complete' in rv_post_confirm.data)


    @mock.patch('application.frontend.server.is_matched', return_value=True)
    @mock.patch('application.frontend.server.is_owner', return_value=False)
    @mock.patch('requests.post')
    @responses.activate
    def test_non_proprieter_cannot_request_change_to_register(self, mock_user_match, mock_owner_check, mock_post):
        #Mock a response, as though JSON is coming back from SEARCH_API
        responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
              body = response_json, status = 200, content_type='application/json')

        # load the form

        self._login('landowner@mail.com', 'password')
        rv = self.client.get('/property/%s/edit/title.proprietor.1' % TITLE_NUMBER, follow_redirects=True)
        self.assertEquals(rv.status_code, 401)


    def tearDown(self):
        self.logout()
        user = User.query.get('landowner@mail.com')
        db.session.delete(user)
        db.session.commit()

class DummyPostData(dict):
    """
    The form wants the getlist method - no problem.
    """
    def getlist(self, key):
        v = self[key]
        if not isinstance(v, (list, tuple)):
            v = [v]
        return v
