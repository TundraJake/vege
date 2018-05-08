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

class BidForm(Form):

	bid = IntegerField('Bid', [validators.NumberRange(min=0, max=100)])
	vege = StringField('Vege Type', [validators.Length(min=0, max=40)])
	bidding_user = IntegerField('Bidding User', [validators.NumberRange(min=100000, max=999999)])