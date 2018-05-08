'''
Author
	Jacob McKenna
Purpose
	UAF CS601 GLORIOUS Web Pages (HW2) Assignemtn

'''

from flask import Flask, request, session, g, redirect, url_for, abort, \
	render_template, flash
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from templates.forms.new_vege import *
from functools import wraps

app = Flask(__name__)
app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
	# DATABASE='mysql://banker:banking@localhost/MuhBank',
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default'
))

app.config.from_envvar('VEGE_SETTINGS', silent=True)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'vege'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)








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

# Home page 
@app.route('/')
@app.route('/home')
def home():
	
	curs = mysql.connection.cursor()
	curs.execute("SELECT * FROM Bids;")
	table = curs.fetchall()

	curs.close()
	return render_template('html/home.html', table=table)


@app.route('/bid', methods=['GET', 'POST'])
def bid():
	form = BidForm(request.form)
	curs = mysql.connection.cursor()

	if request.method == 'POST' and form.validate():
		bid = form.bid.data 
		vege = form.vege.data 
		bidding_user = form.bidding_user.data 

		result = curs.execute("SELECT * FROM Vegetable where name = %s;", [vege])

		if result == 0:
			flash('No vege by that name!', 'error')
			error = 'No veggie by that name!'
			return render_template('html/bid.html', error=error, form=form)


		curs.execute("INSERT INTO Bids (bid, vege, bidding_user) VALUES (%s, %s, %s);", [bid, vege, bidding_user])

		# Commit changes to DB.
		mysql.connection.commit()

		# Close connection! 
		curs.close()

		flash('New Bid is now placed!', 'success')
		
		return redirect(url_for('home'))

	return render_template('html/bid.html', form=form)

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():

	if request.method == 'POST':

		iz = request.form['iz']
		passwordCandidate = request.form['password']

		curs = mysql.connection.cursor()

		result = curs.execute("SELECT * FROM VIP_User where user = %s;", [iz])

		if result > 0:
			data = curs.fetchone()
			hashed_password = data['password']

			# Hash the password candidate and compare hashed_password.
			if sha256_crypt.verify(passwordCandidate, hashed_password):
				session['logged_in'] = True
				session['userid'] = data['user']

				result = curs.execute("SELECT * FROM User where iz = %s;", [iz])
				data = curs.fetchone()
				session['iz'] = data['iz']

				flash('You are now logged in', 'success')
				return redirect(url_for('view_bidderz'))
			else:
				error = 'Invalid login!'
				curs.close()
				return render_template('html/login.html', error=error)
		else:
			error = 'Username not found'
			return render_template('html/login.html', error=error)

	return render_template('html/login.html')

@app.route('/view_bidderz')
@is_logged_in
def view_bidderz():

	curs = mysql.connection.cursor()
	curs.execute("SELECT * FROM User;")
	table = curs.fetchall()
	curs.close()


	return render_template('html/bidderz.html', table=table)


@app.route('/new_vege', methods=['GET', 'POST'])
@is_logged_in
def new_vege():

	# Load the form class by passing request.form to the UserRegisterForm class.
	form = NewVegeForm(request.form)
	curs = mysql.connection.cursor()

	curs.execute("SELECT * FROM Vegetable;")
	vege = curs.fetchall()
	
	if request.method == 'POST' and form.validate():
		vege_name = form.name.data 

		# Create a connection to the DB.
		curs = mysql.connection.cursor()

		result = curs.execute("SELECT * FROM Vegetable WHERE name = %s;", [vege_name])
		# If any results
		if result > 0:
			error = 'This Vege already existz!'
			return render_template('html/new_vege.html', error=error, form=form)

		# If no results, register the new vege. 
		else:

			curs.execute("INSERT INTO Vegetable (name) VALUES (%s);", [vege_name])

			# Commit changes to DB.
			mysql.connection.commit()

			# Close connection! 
			curs.close()

			flash('New Vege is now regiztered', 'success')
			
			return redirect(url_for('new_vege'))

	return render_template('html/new_vege.html', form=form, vege=vege)


@app.route('/new_user', methods=['GET', 'POST'])
def new_user():

	# Load the form class by passing request.form to the UserRegisterForm class.
	form = NewUserForm(request.form)

	if request.method == 'POST' and form.validate():
		firstName = form.fname.data 
		lastName = form.lname.data
		iz = form.iz.data

		# Create a connection to the DB.
		curs = mysql.connection.cursor()

		result = curs.execute("SELECT * FROM User WHERE iz = %s;", [iz])
		# If any results
		if result > 0:
			error = 'This User already existz!'
			return render_template('html/new_user.html', error=error, form=form)

		# If no results, register the new vege. 
		else:
			curs.execute("INSERT INTO User (fname, lname, iz) VALUES (%s, %s, %s);", [firstName, lastName, iz])

			# Commit changes to DB.
			mysql.connection.commit()

			# Close connection! 
			curs.close()

			flash('New User is now regiztered', 'success')
			
			return redirect(url_for('home'))
	return render_template('html/new_user.html', form=form)


# Logout 
@app.route('/logout')
def logout():
	session.clear()
	flash('You are now logged out', 'success')
	return redirect(url_for('home'))

