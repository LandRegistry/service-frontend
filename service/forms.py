from flask_wtf import Form
from wtforms import StringField, DateField, HiddenField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class ChangeForm(Form):

    title_number = HiddenField('Title Number')

    confirm = BooleanField('Confirm')
    proprietor_new_name = StringField('New name', validators=[DataRequired()])
    partner_name = StringField('Partner\'s full name', validators=[DataRequired()])
    marriage_date = StringField('Date of marriage', validators=[DataRequired()])
    marriage_place = StringField('Location of marriage ceremony', validators=[DataRequired()])
    marriage_country = StringField('Country of marriage ceremony', validators=[DataRequired()])
    marriage_certificate_number = StringField('Marriage certificate number', validators=[DataRequired()])

class ConfirmForm(ChangeForm):
    """
    Inherits from ChangeForm and makes all the data caught on the first page hidden.

    """


    title_number = HiddenField('Title Number')

    confirm = BooleanField('Confirm')
    proprietor_new_name = HiddenField('New name')
    partner_name = HiddenField('Partner\'s full name')
    marriage_date = HiddenField('Date of marriage')
    marriage_place = HiddenField('Location of marriage ceremony')
    marriage_country = HiddenField('Country of marriage ceremony', validators=[DataRequired()])
    marriage_certificate_number = HiddenField('Marriage certificate number')
