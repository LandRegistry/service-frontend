from application.frontend.server import app
from application.services import post_to_decision
import mock
import unittest
import datetime


class DecisionTestCase(unittest.TestCase):
    """
    Tests the decision wrapper in decision module.
    """

    def setUp(self):
        self.client = app.test_client()


    @mock.patch('requests.post')
    def test_post(self, mock_post):
        dummy_url = 'dummy'
        dummy_data = {'marriage_country':'GB', 'marriage_date': datetime.datetime.now()}

        with app.test_request_context():
            post_to_decision(dummy_url, dummy_data)

        assert len(mock_post.call_args_list) == 2

