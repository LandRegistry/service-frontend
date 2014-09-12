from datetime import date

from flask import request
from flask_wtf import Form
from wtforms import (
    StringField,
    HiddenField,
    BooleanField,
    DateField,
    PasswordField,
    SubmitField,
    SelectField,
    RadioField,
    TextAreaField
)

from wtforms.validators import DataRequired, ValidationError, NumberRange

from datatypes import country_code_validator
from application.frontend.field_helpers import countries_list_for_selector


class ValidateDateNotInFuture(object):
    def __init__(self):
        self.message = "The date must not be in the future"

    def __call__(self, form, field):
        self._validate_date_not_in_future(form, field.data)

    def _validate_date_not_in_future(self, form, date_field):
        if date_field > date.today():
            raise ValidationError('Date cannot be in the future')


class LoginForm(Form):
    email = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Login')
    remember = BooleanField('Remember me')
    next = HiddenField()

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        if not self.next.data:
            self.next.data = request.args.get('next', '')
        self.remember.default = True


class ChangeForm(Form):
    title_number = HiddenField('Title Number')

    confirm = BooleanField('Confirm')
    proprietor_previous_full_name = HiddenField('Previous full name')
    proprietor_new_full_name = StringField('New full name', validators=[DataRequired()])
    partner_name = StringField('Partner\'s full name', validators=[DataRequired()])
    marriage_date = DateField('Date of marriage', format='%d-%m-%Y',
                              validators=[DataRequired(), ValidateDateNotInFuture()],
                              description="For example, 20-08-2011")
    marriage_place = StringField('Location of marriage ceremony', validators=[DataRequired()])
    marriage_country = SelectField('Country',
                                   validators=[DataRequired(), country_code_validator.wtform_validator()],
                                   choices=countries_list_for_selector)
    marriage_certificate_number = StringField('Marriage certificate number', validators=[DataRequired()])


class ConfirmForm(ChangeForm):
    """
    Inherits from ChangeForm and makes all the data caught on the first page hidden.

    """

    title_number = HiddenField('Title Number')

    confirm = BooleanField('Confirm')
    proprietor_previous_full_name = HiddenField('Previous full name')
    proprietor_new_full_name = HiddenField('New full name')
    partner_name = HiddenField('Partner\'s full name')
    marriage_date = HiddenField('Date of marriage')
    marriage_place = HiddenField('Location of marriage ceremony')
    marriage_country = HiddenField('Country of marriage ceremony')
    marriage_certificate_number = HiddenField('Marriage certificate number')


class ConveyancerAddClientForm(Form):
    full_name = StringField('Full name', validators=[DataRequired()])
    date_of_birth = DateField('Date of birth', format='%d-%m-%Y',
                              validators=[DataRequired(), ValidateDateNotInFuture()],
                              description="For example, 20-08-2011")
    address = TextAreaField('Address', validators=[DataRequired()])
    telephone = StringField('Telephone', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired()])


class SelectTaskForm(Form):
    another_task = StringField('Please specify:')
    buying_or_selling_property = RadioField(
        'Is your client buying or selling this property?',
        choices=[
            ('buying', 'Buying this property'),
            ('selling', 'Selling this property'),
            ('other', 'Another task')
        ])


class ConveyancerAddClientsForm(Form):
    num_of_clients = StringField('How many clients will you act for?',
                                 validators=[DataRequired(),
                                             NumberRange(1, 2, "Number of clients cannot be more than two.")])