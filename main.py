from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

#returns true if a user with the specified email and password exist
def valid_login(email, password): 
	return True # Whoever is in charge of writing code to interact with databases should write this method

#returns an empty list if a user with the specified email does not exist AND the password satisfies the criteria
#otherwise if a user already exists with the specified email, the array should contain the string 'email'
#if the password does not satisfy the criteria then the array should also contain the string 'password'
def valid_registration(email, password):
	return [] # Whoever is in charge of writing code to interact with databases should write this method

#insersts a user with the email and password into database
def insert_user(email, password):
	return # Whoever is in charge of writing code to interact with databases should write this method

@app.route('/login.html', methods=['GET', 'POST'])
def login():
	try: 
		if valid_login(request.form['email'], request.form['password']): #valid email and password provided, forwards user to schedule page
			return render_template('schedule.html')
		else: #invalid username / password
			return render_template('login.html', error=True)
	except KeyError: #runs on initial loading of page, since user has not inputted a username / password
		return render_template('login.html', error=False)

@app.route('/register.html', methods=['GET', 'POST'])
def register():
	try: 
		errors = valid_registration(request.form['email'], request.form['password'])
		if len(errors) == 0:
			return render_template('login.html')
		else:
			return render_template('register.html', errors=errors)
	except:
		return render_template('register.html', error=[])