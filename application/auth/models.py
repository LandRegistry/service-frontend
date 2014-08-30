import json
from datetime import datetime

from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import Enum

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from flask.ext.login import UserMixin

from application import db
from application.services import check_user_match
from application.services import check_user_is_owner


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    email = db.Column(db.String(255), primary_key=True)
    _password = db.Column(db.String(255))

    name = db.Column(TEXT, nullable=False)
    date_of_birth = db.Column(db.Date(), nullable=False)
    gender = db.Column(Enum('F', 'M', name='gender_types'), nullable=False)
    current_address = db.Column(TEXT, nullable=False)
    previous_address = db.Column(TEXT, nullable=False)

    def __repr__(self):
        return str({
            'email': self.email,
            'name': self.name,
            'date of birth': self.date_of_birth,
            'gender': self.gender,
            'current address': self.current_address,
            'previous address': self.previous_address
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

    def loggedin_and_matched(self, password):
        return self.check_password(password) and check_user_match(self)

    def is_owner(self, title_number):
        return check_user_is_owner(self, title_number)

    def to_json_for_match(self):
        return json.dumps({
            'name': self.name,
            'date_of_birth': datetime.strftime(self.date_of_birth, '%Y-%m-%d'),
            'gender' : self.gender,
            'current_address': self.current_address,
            'previous_address': self.previous_address })
