from flask import Flask, render_template, url_for, redirect, request
from flask_wtf import Form
from wtforms import validators, ValidationError
import wtforms
import sqlite3


"""
cursor.execute(''' 
create table user_data 
(name text, gender text, address text, email text, age text, language text) ''')
"""
app = Flask(__name__)
app.secret_key = 'development key'


class ContactForm(Form):
	name = wtforms.TextField("Name Of Student", [validators.Required("Please enter your name.")])
	gender = wtforms.RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
	address = wtforms.TextAreaField("Address")
	email = wtforms.TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
	age = wtforms.IntegerField("age")
	language = wtforms.SelectField('Languages', choices=[('cpp', 'C++'),('py', 'Python')])
	submit = wtforms.SubmitField("Send")

@app.route('/')
def home():
	return redirect(url_for('login'))

@app.route('/info')
def info():
	db = sqlite3.connect('pythondb')
	cursor = db.cursor()
	institute_name = "SCODEEN"''
	cursor.execute("select * from user_data")
	user_data = cursor.fetchall()
	db.commit()
	db.close()
	print("retrived data")
	print(user_data)
	return render_template('home.html', data = user_data)
	
@app.route('/about')
def about():
	return render_template('about.html')
	
@app.route('/register', methods=['GET','POST'])
def register():
	db = sqlite3.connect('pythondb')
	cursor = db.cursor()
	if request.method == 'POST':
		name = request.form['name']
		gender = request.form['gender']
		address = request.form['address']
		email = request.form['email']
		age = request.form['age']
		language = request.form['language']
		cursor.execute(f"INSERT INTO user_data VALUES ('{name}', '{gender}', '{address}', '{email}', '{age}', '{language}')")
		db.commit()
		db.close()
		print(f"INSERT INTO person VALUES ('{name}', '{gender}', '{address}', '{email}', '{age}', '{language}')")
		return redirect(url_for('info'))
	form = ContactForm()
	return render_template('contact.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		username = request.form['uname']
		password = request.form['psw']
		if password == 'abcd':
			return redirect(url_for('info'))
		else:
			return render_template('login.html', msg='Wrong Credentials')

	return render_template('login.html')


if __name__ == '__main__':
	app.run(debug=True, port=5555)