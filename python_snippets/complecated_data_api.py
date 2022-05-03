from flask import Flask
app = Flask(__name__)
import json

@app.route('/')
def index():
    personDetails = [
        {'name': 'John', 'age': 15, 
         'cars': [
             {'name': 'Ford', 'models': ['Fiesta', 'Focus', 'Mustang']},
             {'name': 'Maruti', 'models': ['800', 'Suzuki']},
             {'name': 'Fiat', 'models': ['500', 'Panda']}]},
        {'name': 'chandu', 'age': 23,
         'cars': [
             {'name': 'Tata', 'models': ['Nano', 'Manza']}, 
             {'name': 'BMW', 'models': ['320', 'X3', 'X5']},
             {'name': 'Ferrai', 'models': ['500', 'Panda']}]},
        {'name': 'ashok', 'age': 25,
         'cars': [
             {'name': 'Maruti', 'models': ['800', 'Suzuki']}, 
             {'name': 'BMW', 'models': ['320', 'X3', 'X5']},
             {'name': 'Fiat', 'models': ['500', 'Panda']}]},
        {'name': 'akshay', 'age': 30, 
         'cars': [
             {'name': 'Ford', 'models': ['Fiesta', 'Focus', 'Mustang']},
             {'name': 'BMW', 'models': ['320', 'X3', 'X5']},
            {'name': 'Maruti', 'models': ['800', 'Suzuki']}]}
        ]   
    jsonObj = json.dumps(personDetails) 
    return jsonObj
  
@app.route('/message')
def say_hello():
    return 'Wake_up....!!! Dont Sleep'

if __name__ == "__main__":
    app.run(host='192.168.1.109', debug=True)
