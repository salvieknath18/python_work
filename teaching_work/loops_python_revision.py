l1 = ['abc','ba','c','daa']
"""
for e in l1:
    print(e.count('a'))
    

for i in range(4):
    print(f'ans of {i+1} value')
    print(l1[i].count('a'))

for i,e in enumerate(l1):
    print(f'ans of {i+1} value')
    print(e.count('a'))

l2 = [2,5,78,23,45,48,24,40,43,77,85]
result_list = list()
for i in l2:
    if i%2 == 0 or i%5 == 0:
        result_list.append(i)
    print(result_list)
"""

personDetails = [
                {
                    'name': 'John',
                    'age': 15, 
                    'cars': ['Ford', 'Maruti']
                },
                {
                    'name': 'chandu',
                    'age': 23,
                    'cars': ['Tata', 'BMW']
                },
                {
                    'name': 'ashok',
                    'age': 25,
                    'cars': ['Maruti', 'BFW', 'Ford']
                },
                {
                    'name': 'akshay',
                    'age': 30, 
                    'cars': ['Maruti']
                }
            ]


for person in personDetails:
    for car in person['cars']:
        if "M" in car:
            continue
        print(car)
            






       
        
    

