from flask import Flask, render_template, url_for, redirect, request
import requests
app = Flask(__name__)

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
	return render_template('contact.html')

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