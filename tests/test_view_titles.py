import requests
import responses
import mock
import unittest
import datetime
import uuid

from application.frontend.server import app
from application.frontend import server
from application import db
from application.auth.models import User
from test_samples import title, response_json
from stub_json import (
    response_without_charge,
    response_without_easement
)
from application.services import users

TITLE_NUMBER = "TN1234567"

mock_is_matched = mock.Mock(name='is_matched')
mock_is_matched.return_value = True

@mock.patch.object(users, 'is_matched', mock_is_matched)
class ViewFullTitleTestCase(unittest.TestCase):

    def setUp(self):
        db.drop_all()
        db.create_all()
        self.search_api = app.config['AUTHENTICATED_SEARCH_API']
        self.app = app
        self.client = app.test_client()
        self.lrid = uuid.uuid4()
        self.roles = ['CITIZEN']

    @mock.patch('application.frontend.server.is_within_view_limit', return_value=True)
    @mock.patch('application.frontend.server.get_lrid_and_roles')
    @mock.patch('requests.get')
    def test_get_property_calls_search_api(self, mock_get, mock_user_roles, mock_check_limit):
        mock_user_roles.return_value = self.lrid, self.roles
        mock_get.return_value.json.return_value = title
        self.client.get('/property/%s' % TITLE_NUMBER)

        mock_get.assert_called_with('%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER))

    def test_404(self):
        rv = self.client.get('/pagedoesnotexist')
        assert rv.status == '404 NOT FOUND'

    @mock.patch('application.frontend.server.is_within_view_limit', return_value=True)
    @mock.patch('application.frontend.server.get_lrid_and_roles')
    @mock.patch('requests.get')
    @mock.patch('requests.Response')
    def test_500(self, mock_response, mock_get, mock_user_roles, mock_check_limit):
        mock_user_roles.return_value = self.lrid, self.roles
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
        mock_get.return_value = mock_response
        response = self.client.get('/property/%s' % TITLE_NUMBER)
        assert response.status_code == 500

    @mock.patch('application.frontend.server.is_within_view_limit', return_value=True)
    @mock.patch('application.frontend.server.get_lrid_and_roles')
    @mock.patch('requests.get', side_effect=requests.exceptions.ConnectionError)
    def test_requests_connection_error_returns_500_to_client(self,mock_get, mock_user_roles, mock_check_limit):
        mock_user_roles.return_value = self.lrid, self.roles
        response = self.client.get('/property/%s' % TITLE_NUMBER)
        assert response.status_code == 500

    @mock.patch('application.frontend.server.is_within_view_limit', return_value=True)
    @mock.patch('application.frontend.server.get_lrid_and_roles')
    @responses.activate
    def test_multiple_proprietors(self, mock_user_roles, mock_check_limit):
        mock_user_roles.return_value = self.lrid, self.roles
        responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
              body = response_json, status = 200, content_type='application/json')

        rv = self.client.get('/property/%s' % TITLE_NUMBER, follow_redirects=True)
        assert rv.status_code == 200
        assert 'Bob Test' in rv.data
        assert 'Betty Tanker' in rv.data


    # #TODO charges not in page yet
    # # @responses.activate
    # # def test_charges_appear(self):
    # #     #Mock a response, as though JSON is coming back from SEARCH_API
    # #     responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
    # #           body = response_json, status = 200, content_type='application/json')

    # #     #Now call the usual Service frontend for the same title
    # #     rv = self.client.get('/property/%s' % TITLE_NUMBER, follow_redirects=True)
    # #     assert rv.status_code == 200
    # #     assert 'Charges Register' in rv.data
    # #     assert 'A Transfer of the land in this title dated 01.06.1996 made between Mr Michael Jones and Mr Jeff Smith contains the following provision:-The land has the benefit of a right of way along the passageway to the rear of the property, and also a right of way on foot only on to the open ground on the north west boundary of the land in this title' in rv.data

    @mock.patch('application.frontend.server.is_within_view_limit', return_value=True)
    @mock.patch('application.frontend.server.get_lrid_and_roles')
    @responses.activate
    def test_no_charges_header(self, mock_user_roles, mock_check_limit):
        mock_user_roles.return_value = self.lrid, self.roles
        responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
            body = response_without_charge, status = 200, content_type='application/json')

        rv = self.client.get('/property/%s' % TITLE_NUMBER, follow_redirects=True)
        assert rv.status_code == 200
        assert 'Charges Register' not in rv.data

    @mock.patch('application.frontend.server.is_within_view_limit', return_value=True)
    @mock.patch('application.frontend.server.get_lrid_and_roles')
    @responses.activate
    def test_easements_appear(self, mock_user_roles, mock_check_limit):
        mock_user_roles.return_value = self.lrid, self.roles
        responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
              body = response_json, status = 200, content_type='application/json')

        rv = self.client.get('/property/%s' % TITLE_NUMBER, follow_redirects=True)
        assert rv.status_code == 200
        assert 'Easements' in rv.data

    @mock.patch('application.frontend.server.is_within_view_limit', return_value=True)
    @mock.patch('application.frontend.server.get_lrid_and_roles')
    @responses.activate
    def test_no_easements_header(self, mock_user_roles, mock_check_limit):
        mock_user_roles.return_value = self.lrid, self.roles
        responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
              body = response_without_easement, status = 200, content_type='application/json')

        rv = self.client.get('/property/%s' % TITLE_NUMBER, follow_redirects=True)
        assert rv.status_code == 200
        assert 'Easements Register' not in rv.data

    @mock.patch('application.frontend.server.get_lrid_and_roles')
    @mock.patch('application.frontend.server.is_owner', return_value=False)
    @responses.activate
    def test_view_property_increments_view_count(self, mock_is_owner, mock_user_roles):

        mock_user_roles.return_value = self.lrid, self.roles

        user = User(email='landowner@mail.com',
                     password='password',
                     name='noname',
                     gender='M',
                     date_of_birth=datetime.datetime.now(),
                     current_address='nowhere',
                     previous_address='nowhere',
                     blocked=False,
                     view_count=0)

        db.session.add(user)
        db.session.commit()

        with self.client:
            from flask.ext.login import current_user

            self.client.post('/login', data={'email': user.email, 'password': 'password'}, follow_redirects=True)
            responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
              body = response_json, status = 200, content_type='application/json')

            self.assertEquals(0, current_user.view_count)

            response = self.client.get('/property/%s' % TITLE_NUMBER, follow_redirects=True)

            self.assertEquals(200, response.status_code)
            self.assertEquals(1, current_user.view_count)


    @mock.patch('application.frontend.server.get_lrid_and_roles')
    @mock.patch('application.frontend.server.is_owner', return_value=False)
    @mock.patch('application.services.users.logout_user')
    @responses.activate
    def test_view_property_if_user_exceeds_view_count_redirects_to_login(self, mock_logout, mock_is_owner, mock_user_roles):

        mock_user_roles.return_value = self.lrid, self.roles

        user = User(email='landowner@mail.com',
                     password='password',
                     name='noname',
                     gender='M',
                     date_of_birth=datetime.datetime.now(),
                     current_address='nowhere',
                     previous_address='nowhere',
                     blocked=False,
                     view_count=1)

        db.session.add(user)
        db.session.commit()

        with self.client:
            from flask.ext.login import current_user

            app.config['VIEW_COUNT'] = 1

            self.client.post('/login', data={'email': user.email, 'password': 'password'}, follow_redirects=True)
            responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
              body = response_json, status = 200, content_type='application/json')

            self.assertEquals(1, current_user.view_count)
            response = self.client.get('/property/%s' % TITLE_NUMBER)

            self.assertEquals(302, response.status_code)
            self.assertEquals(response.headers['location'], 'http://localhost/login')
            self.assertTrue(mock_logout.called)


    def test_health(self):
        response = self.client.get('/health')
        assert response.status == '200 OK'

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        db.session.commit()
