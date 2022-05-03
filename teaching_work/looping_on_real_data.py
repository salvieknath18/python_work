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
                 {'name': 'Maruti', 'models': ['1200', 'Suzuki']}, 
                 {'name': 'BMW', 'models': ['320', 'X3', 'X5']},
                 {'name': 'Fiat', 'models': ['500', 'Panda']}]},
            {'name': 'akshay', 'age': 30, 
             'cars': [
                 {'name': 'Ford', 'models': ['fiesta', 'focus', 'Mustang']},
                 {'name': 'BMW', 'models': ['320', 'X3', 'X5']},
                {'name': 'Maruti', 'models': ['800', 'Suzuki']}]}
            ]
result = 0
names = list()
for person in personDetails:
    print(f"******* {person['name']} ******")
    for car in person['cars']:
        print(f"Name: {car['name']} Models: {car['models']}")
    
'''
for person in personDetails:
    for car in person['cars']:
        if car['name']=='BMW' and ('320' in car['models']):
            print(person['name'])
            result = result + 1
            names.append(person['name'])

print(names)
print(result)


for person in personDetails:
    for car in person['cars']:
        for model in car['models']:
            if 'f' in model.lower():
                res_string = f"person: {person['name']} age: {person['age']} car name: {car['name']}" 
                print(res_string)
                names.append(res_string)

print(names)

results = dict()
for person in personDetails:
    model_count = 0
    for car in person['cars']:
        model_count = model_count + len(car['models'])
        # print(f"person: {person['name']} car: {car['name']} car models: {', '.join(car['models'])}")
    results[person['name']] = model_count
print(results)
'''


for i in range(5):
    print("hello")



























