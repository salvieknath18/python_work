'''
Generators
'''
'''
in generator we write a function which has keyword yield
normal function execute complete and return value
but generator functions execute statement upto next yield and then return value
means whenever we call next the function execute for next yield
after executing all yield gives exception
'''
def geneFunc():
    print("first line")
    yield 'A'
    print("second line")
    yield 'B'
    print("third line")
    yield 'C'
    print("fourth line")
    yield 'D'

ob = geneFunc()
print(next(ob))
print("Paused.....")
print(next(ob))
print("Paused.....")
print(next(ob))
print("Paused.....")
print(next(ob))
print("Paused.....Now next will give error")
print(next(ob)) #Yields are finished so now it will give Error

def myGenerator():
    value = 2
    for item in range(10):
        yield item*2

def getPrime(val):
    for i in range(2,val):
        flag = True
        for j in range(2, i):
            if i%j == 0:
                flag = False
        if flag:
            yield i


x = myGenerator()
print(next(x))