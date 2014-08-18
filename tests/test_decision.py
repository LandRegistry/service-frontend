from service.server import app
from service.decision import Decision
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
        
        decision = Decision(dummy_url)
        decision.post(dummy_data)

        assert len(mock_post.call_args_list) == 2

