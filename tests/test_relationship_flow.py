import unittest
import uuid
from application.frontend.server import app


class RelationshipFlowTestCase(unittest.TestCase):

    def setUp(self):
        self.search_api = app.config['AUTHENTICATED_SEARCH_API']
        self.app = app
        self.client = app.test_client()
        self.lrid = uuid.uuid4()
        self.roles = ['CITIZEN']

    def test_conveyancer_flow(self):
        with app.test_request_context():
            response = self.client.get('/relationship/conveyancer')

            self.assertEquals(response.status_code, 200)
            assert '<h1>Create a client relationship</h1>' in response.data
            # TODO: finish testing this flow.