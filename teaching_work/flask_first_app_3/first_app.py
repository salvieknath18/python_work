from flask import Flask, render_template, url_for, redirect, request
from flask_wtf import Form
from wtforms import validators, ValidationError
import wtforms
app = Flask(__name__)
app.secret_key = 'development key'


class ContactForm(Form):
	name = wtforms.TextField("Name Of Student", [validators.Required("Please enter your name.")])
	Gender = wtforms.RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
	Address = wtforms.TextAreaField("Address")
	email = wtforms.TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
	Age = wtforms.IntegerField("age")
	language = wtforms.SelectField('Languages', choices=[('cpp', 'C++'),('py', 'Python')])
	submit = wtforms.SubmitField("Send")

@app.route('/')
def home():
	return redirect(url_for('login'))

@app.route('/info')
def info():
	institute_name = "SCODEEN"''
	student_data = [{'name':'abc','ph':1234,'age':25},
	{'name':'pqu','ph':123436434,'age':15},
	{'name':'safhkj','ph':123634464,'age':30}]
	data = {'i_name': institute_name, 'sdata': student_data}
	return render_template('home.html', data = data)
	
@app.route('/about')
def about():
	return render_template('about.html')
	
@app.route('/contact')
def contact():
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