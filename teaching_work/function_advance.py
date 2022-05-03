#print(list(range(0,101,2)))
def generator_function():
    print("This is A")
    yield 'A'
    print("This is B")
    yield 'B'
    print("This is c")
    yield
    print("This is d")

g = generator_function()
print(next(g))
print(next(g))

def even_number():
    for i in range(0,101,2):
        yield i

e = even_number()
print(next(e))
print(next(e))
print(next(e))

print(next(g))

'''
def decor1(func):
    print("Calling decor 1")
    def inner(num):
        print("Implementing decor 1")
        return func(num)
    return inner

def decor2(func):
    print("Calling decor 2")
    def inner(num):
        print("Implementing decor 2")
        return func(num)
    return inner

@decor2
@decor1
def my_function(num):
    return num


print(my_function(30))

def outer_function(func):
    def inner_function(name):
        if name == "deepak":
            print(f"Bad morning {name}")
        else:
            func(name)
    return inner_function

# With Using Decorator @ symbol
@outer_function
def display(name):
    print(f"hello, Good morning {name}")

display('raj')
display('deepak')

# Without Using Decorator @ symbol
def display1(name):
    print(f"hello, Good morning {name}")

decor_function = outer_function(display1)
decor_function('deepak')



def outer_function(pow_num):
    def power_function(num):
        return num ** pow_num
    return power_function

f1 = outer_function(2)
print(f1(10))
print(f1(20))
f2 = outer_function(3)
print(f2(10))
print(f2(20))


def outer_function():
    print("This is outer function")

    def inner_function():
        print("This is inner function")
        return "inner_string"

    return inner_function

my_new_function = outer_function()
my_new_function()
'''

