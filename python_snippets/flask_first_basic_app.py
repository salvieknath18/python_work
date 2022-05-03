from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def home():
    student_data = [{'name': 'abc', 'ph': 1234, 'age': 25},
                    {'name': 'pqu', 'ph': 123436434, 'age': 15},
                    {'name': 'safhkj', 'ph': 123634464, 'age': 30}]
    return json.dumps(student_data)

@app.route('/info')
def info():
    return "Hello, This is info page"

app.run(debug=True, host="192.168.1.126")