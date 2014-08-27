from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from application import db

class User(db.Model):

    __tablename__ = 'users'

    email = db.Column(db.String(255), primary_key=True)
    _password = db.Column(db.String(255))
    authenticated = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return str({
            'email': self.email
        })

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self , password):
        return check_password_hash(self.password, password)
