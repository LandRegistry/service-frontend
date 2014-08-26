import unittest
import mock

from flask_security.utils import encrypt_password

from application.frontend.server import app
from application import db
from application import user_datastore

from stub_json import title

class AuditTestCase(unittest.TestCase):
    """
    Audit logging must have the 'info' level.
    The tests below will fail if at any point the audit handlers
    use a level that is not 'info'.
    The test will create one test user with ID 1, which the audit
    will report too.
    """
    LOGGER = 'logging.Logger.info'

    def setUp(self):
        app.config["TESTING"] = True,
        app.config["SECRET_KEY"]="no-secret"
        db.drop_all()
        db.create_all()
        self.app = app
        self.client = app.test_client()

        with app.test_request_context():
            user_datastore.create_user(email='landowner@mail.com',
                password=encrypt_password('password'))
            db.session.commit()

    def _login(self, email=None, password=None):
        email = email
        password = password or 'password'
        return self.client.post('/login', data={'email': email, 'password': password},
                         follow_redirects=True)

    #TODO - revisit these tests
    @mock.patch(LOGGER)
    def test_audit_get_index_logs_authenticated_user(self, mock_logger):
        self._login('landowner@mail.com', 'password')
        path = '/'
        self.client.get(path)
        args, kwargs = mock_logger.call_args
        assert 'Audit: ' in args[0]


    @mock.patch(LOGGER)
    @mock.patch('requests.get')
    def test_audit_get_property_page_logs_authenticated_user(self, mock_get, mock_logger):
        mock_get.return_value.json.return_value = title
        self._login('landowner@mail.com', 'password')
        path = '/property/TEST123'
        self.client.get(path)
        assert 'Audit: ' in mock_logger.call_args_list[0][0][0]
