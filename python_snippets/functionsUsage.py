def add1(a,b=100):
		return a+b

add1(2,3)   #5
add1(4)     #104
add1(a=10)  #110
add1(a=10,c=2)
'''
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    add1(a=10,c=2)
TypeError: add1() got an unexpected keyword argument 'c'
'''
def add1(*a,**ka):
	return a+ka

add1(2,3)
'''
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    add1(2,3)
  File "<pyshell#13>", line 2, in add1
    return a+ka
TypeError: can only concatenate tuple (not "dict") to tuple
'''

def add1(*a,**ka):
	return a


add1(2,3)   #(2, 3)

def add1(*a,**ka):
	sum = 0
	for i in a:
		sum += i
	for k,v in ka:
		sum += ka[k]
	for k,v in ka:
		print(k,v)
	return sum

add1(2,3)    #5
add1(2,3,4,8,90)    #107
add1(2,3,4,8,p=90)
'''
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    add1(2,3,4,8,p=90)
  File "<pyshell#27>", line 5, in add1
    for k,v in ka:
ValueError: not enough values to unpack (expected 2, got 1)
'''
def add1(*a,**ka):
	sum = 0
	for i in a:
		sum += i
	for k,v in ka.items():
		sum += ka[k]
	for k,v in ka.items():
		print(k,v)
	return sum

add1(2,3,4,8,p=90)    #p 90  107
add1(2,3,4,q=8,p=90)   #q 8  p 90 107

def add1(*a,**ka):
	sum = 0
	for i in a:
		sum += i
	for k,v in ka.items():
		sum += ka[k]
	for k,v in ka.items():
		print(k,v)
	print(ka)
	return sum

add1(2,3,4,q=8,p=90)
'''
q 8
p 90
{'q': 8, 'p': 90}
107
'''

'''
****************************               Lambda Map Filter and reduce 
'''


s = lambda x:x*x
'''
s(2)
ans = 4
'''
s = lambda a,b: a if a>b else b
'''
s(3,4)
ans = 4
'''

map(lambda x:x*x, [1,2,3,4,5])
#<map object at 0x7ffa910776a0>

list(map(lambda x:x*x, [1,2,3,4,5]))
#[1, 4, 9, 16, 25]

list(map(lambda x:x*x if x%2==0 else 0, [1,2,3,4,5]))
#[0, 4, 0, 16, 0]

list(map(lambda x:x if x%2==0 else 0, [1,2,3,4,5]))
#[0, 2, 0, 4, 0]
'''
map operate the lambda function to every element of list and returns the result list
'''

filter(lambda x:x if x%2==0 else 0, [1,2,3,4,5])
#<filter object at 0x7ffa91084278>

list(filter(lambda x:x if x%2==0 else 0, [1,2,3,4,5]))
#[2, 4]

list(filter(lambda x:x*x if x%2==0 else 0, [1,2,3,4,5]))
#[2, 4]

list(filter(lambda x:x*x if x%2==0 else 1, [1,2,3,4,5]))
#[1, 2, 3, 4, 5]
'''
from above example filter filters the value in the list for which function returns true
'''

list(map(lambda x:x%2==0, [1,2,3,4,5]))
[False, True, False, True, False]

list(filter(lambda x:x%2==0, [1,2,3,4,5]))
#[2, 4]


def add(a,b,c):
	sum = a+b+c
	print('SUM:',sum)

l =[1,2,3]
add(*l)

def add(*a):
	sum = a[0]+a[1]+a[2]
	print('SUM:',sum)

ad =add(1,2,3)
