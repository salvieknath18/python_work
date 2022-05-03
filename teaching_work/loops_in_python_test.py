Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: D:/scodeen/pythondata/P6/looping_on_real_data.py =========
>>> personDetails[0]
{'name': 'John', 'age': 15, 'cars': [{'name': 'Ford', 'models': ['Fiesta', 'Focus', 'Mustang']}, {'name': 'Maruti', 'models': ['800', 'Suzuki']}, {'name': 'Fiat', 'models': ['500', 'Panda']}]}
>>> personDetails[0].keys()
dict_keys(['name', 'age', 'cars'])
>>> personDetails[0]['age']
15
>>> personDetails[1]['cars']
[{'name': 'Tata', 'models': ['Nano', 'Manza']}, {'name': 'BMW', 'models': ['320', 'X3', 'X5']}, {'name': 'Ferrai', 'models': ['500', 'Panda']}]
>>> personDetails[1]['cars'][0]
{'name': 'Tata', 'models': ['Nano', 'Manza']}
>>> personDetails[1]['cars'][0]['models']
['Nano', 'Manza']
>>> for person in personDetails:
	print(person)

	
{'name': 'John', 'age': 15, 'cars': [{'name': 'Ford', 'models': ['Fiesta', 'Focus', 'Mustang']}, {'name': 'Maruti', 'models': ['800', 'Suzuki']}, {'name': 'Fiat', 'models': ['500', 'Panda']}]}
{'name': 'chandu', 'age': 23, 'cars': [{'name': 'Tata', 'models': ['Nano', 'Manza']}, {'name': 'BMW', 'models': ['320', 'X3', 'X5']}, {'name': 'Ferrai', 'models': ['500', 'Panda']}]}
{'name': 'ashok', 'age': 25, 'cars': [{'name': 'Maruti', 'models': ['800', 'Suzuki']}, {'name': 'BMW', 'models': ['320', 'X3', 'X5']}, {'name': 'Fiat', 'models': ['500', 'Panda']}]}
{'name': 'akshay', 'age': 30, 'cars': [{'name': 'Ford', 'models': ['Fiesta', 'Focus', 'Mustang']}, {'name': 'BMW', 'models': ['320', 'X3', 'X5']}, {'name': 'Maruti', 'models': ['800', 'Suzuki']}]}
>>> for person in personDetails:
	print(person['age'])

	
15
23
25
30
>>> for person in personDetails:
	print(person['name'])

	
John
chandu
ashok
akshay
>>> for person in personDetails:
	print(f"Name of person is {} and age is person['name']{person['age']}")
	
SyntaxError: f-string: empty expression not allowed
>>> 
>>> for person in personDetails:
	print(f"Name of person is {person['name']} and age is {person['age']}")

	
Name of person is John and age is 15
Name of person is chandu and age is 23
Name of person is ashok and age is 25
Name of person is akshay and age is 30
>>> for person in personDetails:
	print(f"Name of person is {person['name']} and age is {person['age']}")

	
Name of person is John and age is 15
Name of person is chandu and age is 23
Name of person is ashok and age is 25
Name of person is akshay and age is 30
>>> for person in personDetails:
	for car in person['cars']:
		if car['name'] == "Maruti":
			print(person['name'])

			
John
ashok
akshay
>>> for person in personDetails:
	for car in person['cars']:
		if "Maruti" in car.values():
			print(person['name'])

			
John
ashok
akshay
>>> for person in personDetails:
	for car in person['cars']:
		if '800' in car['models']:
			print(person['name'])

			
John
ashok
akshay
>>> 
========= RESTART: D:/scodeen/pythondata/P6/looping_on_real_data.py =========
>>> for person in personDetails:
	for car in person['cars']:
		if '800' in car['models']:
			print(person['name'])

			
John
akshay
>>> 
