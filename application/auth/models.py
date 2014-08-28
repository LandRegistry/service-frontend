from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import Enum

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from flask.ext.login import UserMixin

from application import db
from application.services import check_user_match

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    email = db.Column(db.String(255), primary_key=True)
    _password = db.Column(db.String(255))

    lrid = db.Column(UUID(as_uuid=True), nullable=False, primary_key=True)
    name = db.Column(TEXT, nullable=False)
    date_of_birth = db.Column(db.Date(), nullable=False)
    gender = db.Column(Enum('F', 'M', name='gender_types'), nullable=False)
    current_address = db.Column(TEXT, nullable=False)
    previous_address = db.Column(TEXT, nullable=False)

    def __repr__(self):
        return str({
            'email': self.email
        })

    def get_id(self):
        return self.email

    @property
    def password(self):
        raise AttributeError("Password not readable")

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self , password):
        return check_password_hash(self._password, password)

    def loggedin_and_matched(self):
        return self.check_password() and check_user_match(self)
