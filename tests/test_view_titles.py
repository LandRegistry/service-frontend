import requests
import responses
import mock
import unittest
import datetime


from application.frontend.server import app
from application.frontend import server
from application import db
from application.auth.models import User
from test_samples import title, response_json
from stub_json import ( response_without_charge,
                        response_without_easement
)

TITLE_NUMBER = "TN1234567"

mock_is_matched = mock.Mock(name='is_matched')
mock_is_matched.return_value = True

@mock.patch.object(server, 'is_matched', mock_is_matched)
class ViewFullTitleTestCase(unittest.TestCase):

    def setUp(self):
        db.drop_all()
        db.create_all()
        self.search_api = app.config['AUTHENTICATED_SEARCH_API']
        self.app = app
        self.client = app.test_client()

    @mock.patch('requests.get')
    def test_get_property_calls_search_api(self, mock_get):
        mock_get.return_value.json.return_value = title
        self.client.get('/property/%s' % TITLE_NUMBER)

        mock_get.assert_called_with('%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER))

    def test_404(self):
        rv = self.client.get('/pagedoesnotexist')
        assert rv.status == '404 NOT FOUND'

    @mock.patch('requests.get')
    @mock.patch('requests.Response')
    def test_500(self, mock_response, mock_get):

        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
        mock_get.return_value = mock_response
        response = self.client.get('/property/%s' % TITLE_NUMBER)
        assert response.status_code == 500


    @mock.patch('requests.get', side_effect=requests.exceptions.ConnectionError)
    def test_requests_connection_error_returns_500_to_client(self,mock_get):
        response = self.client.get('/property/%s' % TITLE_NUMBER)
        assert response.status_code == 500


    @responses.activate
    def test_multiple_proprietors(self):
        #Mock a response, as though JSON is coming back from SEARCH_API
        responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
              body = response_json, status = 200, content_type='application/json')

        #Now call the usual Service frontend for the same title.  Redirects
        #to the mocked response in HTML.

        rv = self.client.get('/property/%s' % TITLE_NUMBER, follow_redirects=True)
        assert rv.status_code == 200
        assert 'Bob Test' in rv.data
        assert 'Betty Tanker' in rv.data

    @responses.activate
    def test_charges_appear(self):
        #Mock a response, as though JSON is coming back from SEARCH_API
        responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
              body = response_json, status = 200, content_type='application/json')

        #Now call the usual Service frontend for the same title
        rv = self.client.get('/property/%s' % TITLE_NUMBER, follow_redirects=True)
        assert rv.status_code == 200
        assert 'Charges Register' in rv.data
        assert 'A Transfer of the land in this title dated 01.06.1996 made between Mr Michael Jones and Mr Jeff Smith contains the following provision:-The land has the benefit of a right of way along the passageway to the rear of the property, and also a right of way on foot only on to the open ground on the north west boundary of the land in this title' in rv.data

    @responses.activate
    def test_no_charges_header(self):
      #Mock a response, as though JSON is coming back from SEARCH_API
      responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
            body = response_without_charge, status = 200, content_type='application/json')

      #Now call the usual Service frontend for the same title.
      rv = self.client.get('/property/%s' % TITLE_NUMBER, follow_redirects=True)
      assert rv.status_code == 200
      assert 'Charges Register' not in rv.data

    @responses.activate
    def test_easements_appear(self):
        #Mock a response, as though JSON is coming back from SEARCH_API
        responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
              body = response_json, status = 200, content_type='application/json')

        #Now call the usual Service frontend for the same title
        rv = self.client.get('/property/%s' % TITLE_NUMBER, follow_redirects=True)
        assert rv.status_code == 200
        assert 'Easements Register' in rv.data
        assert 'easement one' in rv.data
        assert 'easement two' in rv.data

    @responses.activate
    def test_no_easements_header(self):
      #Mock a response, as though JSON is coming back from SEARCH_API
      responses.add(responses.GET, '%s/auth/titles/%s' % (self.search_api, TITLE_NUMBER),
            body = response_without_easement, status = 200, content_type='application/json')

      #Now call the usual Service frontend for the same title

      rv = self.client.get('/property/%s' % TITLE_NUMBER, follow_redirects=True)
      assert rv.status_code == 200
      assert 'Easements Register' not in rv.data


    def test_health(self):
        response = self.client.get('/health')
        assert response.status == '200 OK'
