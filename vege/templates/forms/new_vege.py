from wtforms import Form, BooleanField, TextField, HiddenField, PasswordField,\
DateTimeField, validators, IntegerField, SubmitField, SelectField, StringField

from flask_wtf import FlaskForm

# User registration. 
class NewVegeForm(Form):

	name = StringField('Vege Name', [validators.Length(min=0, max=40)])

class NewUserForm(Form):

	fname = StringField('First Name', [validators.Length(min=0, max=40)])
	lname = StringField('Last Name', [validators.Length(min=0, max=40)])
	iz = IntegerField('Iz Number', [validators.NumberRange(min=100000, max=999999)])