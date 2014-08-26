from flask_wtf import Form
from wtforms import StringField, HiddenField, BooleanField, DateField
from wtforms.validators import DataRequired
from fields import CountriesField
from datetime import date
from wtforms.validators import ValidationError


class ValidateDateNotInFuture(object):
    def __init__(self):
        self.message = "The date must not be in the future"

    def __call__(self, form, field):
        self._validate_date_not_in_future(form, field.data)

    def _validate_date_not_in_future(self, form, date_field):
        if date_field > date.today():
            raise ValidationError('Date cannot be in the future')


class ChangeForm(Form):

    title_number = HiddenField('Title Number')

    confirm = BooleanField('Confirm')
    proprietor_firstname = HiddenField('First name')
    proprietor_previous_surname = HiddenField('Previous surname')
    proprietor_new_surname = StringField('New surname', validators=[DataRequired()])
    partner_name = StringField('Partner\'s full name', validators=[DataRequired()])
    marriage_date = DateField('Date of marriage', format='%d-%m-%Y', validators=[DataRequired(), ValidateDateNotInFuture()], description="For example, 20-08-2011")
    marriage_place = StringField('Location of marriage ceremony', validators=[DataRequired()])
    #marriage_country = CountriesField('Country of marriage ceremony', validators=[DataRequired()], top_countries=['GB'])
    marriage_country = StringField('Country of marriage ceremony', validators=[DataRequired()])
    marriage_certificate_number = StringField('Marriage certificate number', validators=[DataRequired()])


class ConfirmForm(ChangeForm):
    """
    Inherits from ChangeForm and makes all the data caught on the first page hidden.

    """

    title_number = HiddenField('Title Number')

    confirm = BooleanField('Confirm')
    proprietor_firstname = HiddenField('First name')
    proprietor_previous_surname = HiddenField('Previous surname')
    proprietor_new_surname = HiddenField('New surname')
    partner_name = HiddenField('Partner\'s full name')
    marriage_date = HiddenField('Date of marriage')
    marriage_place = HiddenField('Location of marriage ceremony')
    marriage_country = HiddenField('Country of marriage ceremony')
    marriage_certificate_number = HiddenField('Marriage certificate number')
