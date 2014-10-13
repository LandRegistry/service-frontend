from flask_wtf import Form
from wtforms import (
    StringField,
    DateField,
    SelectField,
    RadioField,
    TextAreaField
)

from wtforms.validators import DataRequired, Email

class ConveyancerAddClientForm(Form):
    full_name = StringField('Full name', validators=[DataRequired()])
    date_of_birth = DateField('Date of birth', format='%d-%m-%Y',
                              validators=[DataRequired()],
                              description="For example, 20-08-2011")
    address = TextAreaField('Address', validators=[DataRequired()])
    telephone = StringField('Telephone', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired(), Email()])

    # this is temporary for matching
    gender = SelectField('Gender', choices=[('', 'Select gender'),('F', 'Female'), ('M', 'Male')], validators=[DataRequired()])



class SelectTaskForm(Form):
    buying_or_selling_property = RadioField(
        'Is your client buying or selling this property?',
        choices=[
            ('buying', 'Buying this property'),
            ('selling', 'Selling this property')
        ],
        validators=[DataRequired()])
