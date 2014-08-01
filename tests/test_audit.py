import unittest
import mock
import flask
from service.server import app
from flask_security.utils import encrypt_password
from service import db
from service import user_datastore


class AuditTestCase(unittest.TestCase):
    """
    Audit logging must have the 'info' level.
    The tests below will fail if at any point the audit handlers
    use a level that is not 'info'.
    The test will create one test user with ID 1, which the audit
    will report too.
    """
    LOGGER = 'logging.Logger.info'
    ANON_GET_TEMPLATE = "Audit: user=[{'id': '1', 'email': 'landowner@mail.com'}], request=[<Request 'http://localhost%s' [GET]>]"

    def setUp(self):
        app.config["TESTING"] = True,
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


    @mock.patch(LOGGER)
    def test_audit_get_index(self, mock_logger):
        self._login('landowner@mail.com', 'password')
        path = '/'
        self.client.get(path)
        mock_logger.assert_called_with(self.ANON_GET_TEMPLATE % path)


    @mock.patch(LOGGER)
    def test_audit_get_registration(self, mock_logger):
        self._login('landowner@mail.com', 'password')
        path = '/registration'
        self.client.get(path)
        mock_logger.assert_called_with(self.ANON_GET_TEMPLATE % path)
