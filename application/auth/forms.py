from flask import request

from flask_wtf import Form

from wtforms import (
    StringField,
    HiddenField,
    PasswordField,
    SubmitField
)

from wtforms.validators import (
    DataRequired,
    Email
)

class LoginForm(Form):
    email = StringField('User name', validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Sign in')
    next = HiddenField()

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        if not self.next.data:
            self.next.data = request.args.get('next', '')
