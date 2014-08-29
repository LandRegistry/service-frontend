from application.frontend.server import app
from application import db
from application.auth.models import User

import mock
import responses
import unittest

from stub_json import response_json

TITLE_NUMBER = "TN1234567"

class ChangeTitleTestCase(unittest.TestCase):

    def setUp(self):
        db.drop_all()
        db.create_all()
        self.search_api = app.config['AUTHENTICATED_SEARCH_API']
        self.client = app.test_client()

        user = User(email='landowner@mail.com',
                password='password')
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
            form['proprietor_previous_full_name'] = 'Proprietor Previous Full Name'
            form['proprietor_new_full_name'] = 'Proprietor New full name'
            form['partner_name'] = 'Partner Name'
            form['marriage_date'] = '01-01-2014'
            form['marriage_place'] = 'Testville'
            form['marriage_country'] = 'GB'
            form['marriage_certificate_number'] = '00000000'
            return form


    #TODO - have a look at this test again
    @mock.patch('requests.post')
    @responses.activate
    def test_change_register(self, mock_post):
        #Mock a response, as though JSON is coming back from SEARCH_API
        responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
              body = response_json, status = 200, content_type='application/json')

        # load the form

        self._login('landowner@mail.com', 'password')
        rv = self.client.get('/property/%s/edit/title.proprietor.1' % TITLE_NUMBER, follow_redirects=True)
        assert rv.status_code == 200
        assert 'Change register' in rv.data

        # post the change

        form = self.get_unconfirmed_change_form()
        rv_post = self.client.post(
            '/property/%s/edit/title.proprietor.1' % TITLE_NUMBER,
            follow_redirects=True,
            data=DummyPostData(form))
        assert rv_post.status_code == 200
        assert 'I confirm that I' in rv_post.data

        # confirm

        form['confirm'] = True
        rv_post_confirm = self.client.post(
            '/property/%s/edit/title.proprietor.1' % TITLE_NUMBER,
            follow_redirects=True,
            data=DummyPostData(form))
        assert rv_post_confirm.status_code == 200
        assert 'Application complete' in rv_post_confirm.data

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
