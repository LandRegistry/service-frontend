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
    marriage_certificate_number = StringField('Marriage certificate number', validators=[DataRequired()])
    witness_name = StringField('Full name of witness', validators=[DataRequired()])
    witness_address = TextAreaField('Address of witness', validators=[DataRequired()])
    witness2_name = StringField('Full name of second witness', validators=[DataRequired()])
    witness2_address = TextAreaField('Address of second witness', validators=[DataRequired()])

class ConfirmForm(ChangeForm):

    title_number = HiddenField('Title Number')

    confirm = BooleanField('Confirm')

    proprietor_new_name = HiddenField('New name')
    partner_name = HiddenField('Partner\'s full name')
    marriage_date = HiddenField('Date of marriage')
    marriage_place = HiddenField('Location of marriage ceremony')
    marriage_certificate_number = HiddenField('Marriage certificate number')
    witness_name = HiddenField('Full name of witness')
    witness_address = HiddenField('Address of witness')
    witness2_name = HiddenField('Full name of second witness')
    witness2_address = HiddenField('Address of second witness')
