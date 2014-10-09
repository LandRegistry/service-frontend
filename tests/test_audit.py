import unittest
import mock
import datetime
import uuid

from application import db
from application.frontend.server import app
from application.auth.models import User

from test_samples import title

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
        db.drop_all()
        db.create_all()
        self.app = app
        self.client = app.test_client()

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
        self.lrid = uuid.uuid4()
        self.roles = ['CITIZEN']

    def login(self, email=None, password=None):
        password = password or 'password'
        return self.client.post('/auth/login', data={'email': email, 'password': password}, follow_redirects=True)

    def logout(self):
        return self.client.get('/auth/logout', follow_redirects=True)


    @mock.patch(LOGGER)
    @mock.patch('requests.post')
    def test_audit_get_index_logs_authenticated_user(self, mock_post, mock_logger):
        mock_post.return_value.json.return_value = {"lrid":self.lrid, "roles":self.roles}
        self.login('landowner@mail.com', 'password')
        path = '/'
        self.client.get(path)
        args, kwargs = mock_logger.call_args
        self.assertTrue(str(self.lrid) in args[0])
        self.assertTrue('landowner@mail.com' in args[0])

    @mock.patch(LOGGER)
    @mock.patch('requests.post')
    @mock.patch('requests.get')
    @mock.patch('application.frontend.server.is_owner', return_value=True)
    def test_audit_get_property_page_logs_authenticated_user(self, mock_owner_check, mock_get,mock_post, mock_logger):
        mock_post.return_value.json.return_value = {"lrid":self.lrid, "roles":self.roles}
        mock_get.return_value.json.return_value = title
        self.login('landowner@mail.com', 'password')
        path = '/property/TEST123'
        self.client.get(path)
        args, kwargs = mock_logger.call_args
        self.assertTrue(str(self.lrid) in args[0])
        self.assertTrue('landowner@mail.com' in args[0])
        self.assertTrue(path in args[0])

    def tearDown(self):
        self.logout() #to ensure no-one is logged in after a test is run
        user = User.query.get('landowner@mail.com')
        db.session.delete(user)
        db.session.commit()
