from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
import json
import datetime
import os
import database

app = Flask(__name__)
app.secret_key = os.urandom(16)

times= ['8:00AM', '9:00AM', '10:00AM', '11:00AM', '12:00PM', '1:00PM', '2:00PM', '3:00PM', '4:00PM', '5:00PM', '6:00PM', '7:00PM']

def valid_password(password):
	return any(c.isdigit() for c in password) and password != password.lower() and password != password.upper()

#returns true if a user with the specified email and password exist
def valid_login(email, password): 
	return database.db_Login(email, password)

#returns an empty list if a user with the specified email does not exist AND the password satisfies the criteria
#otherwise if a user already exists with the specified email, the array should contain the string 'email'
#if the password does not satisfy the criteria then the array should also contain the string 'password'
def valid_registration(email, password):
	errs = []
	if not valid_password(password):
		errs.append('password')

	if database.db_account_exists(email):
		errs.append('email')
	
	if len(errs) == 0:
		database.db_account_Store(email, password)
	return errs

#insersts a user with the email and password into database
def insert_user(email, password):
	return # Whoever is in charge of writing code to interact with databases should write this method

def format_date(date):
	return str(date.month) + '-' + str(date.day) + '-' + str(date.year)

@app.route('/login', methods=['GET', 'POST'])
def login():
	try: 
		if valid_login(request.form['email'], request.form['password']): #valid email and password provided, forwards user to schedule page
			session['user'] = {'email' : request.form['email'], 'tasks': []}
			return redirect(url_for('viewSchedule'))
		else: #invalid username / password
			return render_template('login.html', error=True)
	except KeyError: #runs on initial loading of page, since user has not inputted a username / password
		return render_template('login.html', error=False)

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html', errors = [])

	errors = valid_registration(request.form['email'], request.form['password'])
	if len(errors) == 0:
		return redirect('login')
	else:
		return render_template('register.html', errors=errors)

@app.route('/viewSchedule', methods=['GET', 'POST'])
def viewSchedule():
	if 'user' not in session:
		return redirect('/login')
	if request.form == 'POST':
		now = request.form['date']
	else:
		now = datetime.datetime.now()
	dates = []
	for i in range(0,7):
		tempDate = now + datetime.timedelta(days=i)
		dates.append(format_date(tempDate))
	return render_template('schedule.html', user = session['user'], dates = dates, times = times)

@app.route('/addTask', methods=['GET', 'POST'])
def addTask():
	return render_template('addTask.html', times=times)

@app.route('/removeTask', methods=['GET', 'POST'])
def removeTask():
	if 'user' not in session:
		return redirect('/login')
	return render_template('removeTask.html', user = session['user'], times=times)

@app.route('/')
def index():
	return redirect('/login')