import json

from datetime import datetime

from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.types import Enum

from sqlalchemy.dialects.postgresql import BOOLEAN

from flask.ext.login import UserMixin

from application import (
    db,
    app
)

from lrutils import PasswordUtils
password_utils = PasswordUtils(app.config)

class User(db.Model, UserMixin):

    __tablename__ = 'lr_users'

    email = db.Column(db.String(255), primary_key=True)
    _password = db.Column(db.String(255))

    name = db.Column(TEXT, nullable=False)
    date_of_birth = db.Column(db.Date(), nullable=False)
    gender = db.Column(Enum('F', 'M', name='gender_types'), nullable=False)
    current_address = db.Column(TEXT, nullable=False)
    previous_address = db.Column(TEXT, nullable=False)
    blocked = db.Column(BOOLEAN, nullable=False)
    view_count = db.Column(db.Integer, nullable=False)

    def get_id(self):
        return self.email

    @property
    def password(self):
        raise AttributeError("Password not readable")

    @password.setter
    def password(self, password):
        self._password = password_utils.encrypt_password(password)

    def check_password(self , password):
        return password_utils.verify_password(password, self._password)

    def to_json_for_match(self):
        return json.dumps({
            'name': self.name,
            'date_of_birth': datetime.strftime(self.date_of_birth, '%Y-%m-%d'),
            'gender' : self.gender,
            'current_address': self.current_address,
            'previous_address': self.previous_address})
