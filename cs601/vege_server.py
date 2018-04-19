'''
Author
	Jacob McKenna
Purpose
	UAF CS601 GLORIOUS Web Pages (HW2) Assignemtn

'''

import pymongo
from flask import Flask

app = Flask(__name__)


# Check if the user is logged in. 
# Need this to 
def is_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('Unauthorized, Please login', 'danger')
			return redirect(url_for('login'))
	return wrap

@app.route("/bids")
def hello():
    return "Bids"

@app.route("/login")
def enter():
	return "Login Page"
