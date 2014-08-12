from flask_wtf import Form
from wtforms import StringField, DateField, HiddenField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class ChangeForm(Form):

    title_number = HiddenField('Title Number')

    confirm = BooleanField('Confirm')

    proprietor_new_name = StringField('New name', validators=[DataRequired()])
    partner_name = StringField('Partner\'s full name', validators=[DataRequired()])
    marriage_date = DateField('Date of marriage', format='%Y-%m-%d', validators=[DataRequired()])
    marriage_place = StringField('Location of marriage ceremony', validators=[DataRequired()])
    marriage_certificate_number = StringField('Marriage certificate number', validators=[DataRequired()])
    witness_name = StringField('Full name of witness', validators=[DataRequired()])
    witness_address = TextAreaField('Address of witness', validators=[DataRequired()])
    witness2_name = StringField('Full name of second witness', validators=[DataRequired()])
    witness2_address = TextAreaField('Address of second witness', validators=[DataRequired()])
