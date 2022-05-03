''' Variable scope'''
'''
a = 10
b = 20
def f1():
    global c
    global a
    print("Print a inside 1: ", a)
    a = 15
    c = 30
    print("Print a inside 2: ", a)
    print("Print b inside 1: ", b)


print("Print a outside 1: ", a)
f1()
print("Print a outside 2: ", a)
print("Print c outside 1: ", c)

'''
'''Types of arguments'''
'''
def add1(a, b, c)
    ans = a+b+c
    print(ans)
    return ans
add1(10, 20, 30)

def add1(a, b, c)
    ans = a+b+c
    print(ans)
    return ans
add1(10, b=20, c=30)
add1(10, c=30, b=40)

def add1(a, b, c= 100)
    ans = a+b+c
    print(ans)
    return ans
add1(10, b=20, c=30)
add1(10, b=20)



def add1(*args):
    print(args)
    mul = 1
    for arg in args:
        mul = mul * arg
    ans = sum(args)
    print(ans, mul)
    return ans

add1(10, 20, 30)

def add1(args):
    print(args)
    mul = 1
    for arg in args:
        mul = mul * arg
    ans = sum(args)
    print(ans, mul)
    return ans

n = input("Enter how many numbers to add")
inp_data = list()
for i in range(int(n)):
    inp_data.append(int(input(f"Enter number {i+1} : ")))
    
add1(inp_data)

def add1(a,b,c,d):
    ans = a+b+c+d
    return ans

inp_data = (10,20,30,40)
res = add1(*inp_data)
print(res * res)
'''
def add1(*args, **kwargs):
    print(args)
    print(kwargs)
    for k, v in kwargs.items():
        print(f"{k} is {v}")
    mul = 1
    for arg in args:
        mul = mul * arg
    ans = sum(args)
    print(ans, mul)
    return ans

add1(10, 20, 30, name='abcd', age=25, phone_no=2524214)









    
