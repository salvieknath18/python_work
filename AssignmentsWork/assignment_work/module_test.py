'''
This is my test module
it will  have some basic functions
like add sub
'''
from os import getcwd

def add(a,b):
    '''
    this is addition function adds two numbers
    a & b --> a + b
    '''
    print "addition is: ", a + b
    return a+b

def sub(a,b):
    '''
    this is subtraction function adds two numbers
    a & b --> a - b
    '''
    print "subtraction is: ", a - b
    return a-b

pi = 3.15
e = 1000


if __name__ == '__main__':
    print "hello"
