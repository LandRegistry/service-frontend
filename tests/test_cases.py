from application.frontend.server import app
from application.services import post_to_cases
import mock
import unittest
import datetime


class CasesTestCase(unittest.TestCase):
    """
    Tests the cases wrapper in cases module.
    """

    def setUp(self):
        app.config["CASES_URL"] = 'http://nowhere'
        self.client = app.test_client()


    @mock.patch('requests.post')
    def test_post(self, mock_post):
        dummy_data = {'title_number': 'TEST123', 'proprietor_full_name': 'Bob', 'marriage_country': 'GB', 'marriage_date': datetime.datetime.now()}

        with app.test_request_context():
            post_to_cases('the-action', dummy_data)

        assert len(mock_post.call_args_list) == 1
