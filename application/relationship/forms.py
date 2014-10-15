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
    telephone = StringField('Mobile phone number', validators=[DataRequired()], description="this may be used to receive security codes")
    email = StringField('Email address', validators=[DataRequired(), Email()])

    # this is temporary for matching
    gender = RadioField('Gender', choices=[('F', 'Female'), ('M', 'Male')], validators=[DataRequired()])


class SelectTaskForm(Form):
    buying_or_selling_property = RadioField(
        'Is your client buying or selling this property?',
        choices=[
            ('buying', 'Buying'),
            ('selling', 'Selling')
        ],
        validators=[DataRequired()])
