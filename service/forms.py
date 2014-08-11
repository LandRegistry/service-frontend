from flask_wtf import Form
from wtforms import StringField, DateField, HiddenField, TextAreaField
from wtforms.validators import DataRequired

class ChangeForm(Form):

    title_number = HiddenField('Title Number')
    proprietor_new_name = StringField('New name', validators=[DataRequired()])
    partner_full_name = StringField('Partner\'s full name', validators=[DataRequired()])
    date_of_marriage = DateField('Date of marriage', format='%Y-%m-%d', validators=[DataRequired()])
    location_of_marriage_ceremony = StringField('Location of marriage ceremony', validators=[DataRequired()])
    marriage_certificate_number = StringField('Marriage certificate number', validators=[DataRequired])
    witness_full_name = StringField('Full name of witness', validators=[DataRequired])

    witness_house_number = TextAreaField('Address of witness', validators=[DataRequired()])

