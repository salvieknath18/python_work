pydata = {
    "name": "John",
    "age": 30,
    "cars": [
        {"name": "Ford", "models": ["Fiesta", "Focus", "Mustang"]},
        {"name": "BMW", "models": ["320", "X3", "X5"]},
        {"name": "Fiat", "models": ["500", "Panda"]}
    ]}
"""
for car in pydata['cars']:
    print(car['name']+ " - ", end="")
    for model in car["models"]:
        print(model + ", ", end="")
    print()

for car in pydata['cars']:
    print(car['name']+ " - ", ":".join(car["models"]))

car_list = list()
for car in pydata['cars']:
    car_list.append(car['name'])

for car in pydata['cars']:
    for model in car['models']:
        for chr in model:
            print(chr)
            

print({car['name']:model for car in pydata['cars'] for model in car['models']})


print([i for i in [7, 5, 35, 70, 140, 50] if i%5 == 0 and i%7 == 0])

l1 = [7, 5, 35, 70, 140, 50]
for e in l1:
    if e%5==0 and e%7==0:
        print(e)

def myfunction(e):
    if e%5==0 and e%7==0:
        return True
    else:
        return False


def myfunction_withAnnotaion(e: int) -> bool:
    if e % 5 == 0 and e % 7 == 0:
        return True
    else:
        return False

print(myfunction.__annotations__)
print(myfunction_withAnnotaion.__annotations__)


print(list(filter(myfunction, l1)))

l2 = [1, 3, 4, 15, 16, 25, 50]

print(list(map(lambda a: a*a, l2)))

def sqr(a):
    return a*a

print(list(map(sqr, l2)))
"""

