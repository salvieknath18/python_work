'''
Closure
'''

def outerFunction(num1):

    def innerFunction(num2):
        return num2 ** num1

    return innerFunction

x2 = outerFunction(2) #num1 will be 2
print(x2(10))   #num2 will be 10 and num1 = 2

print(x2(20))  #num2 will be 20 and num1 = 2
'''
the value num1 is 2 is carreid in both the statement
Hence Closue is used to attach value with function
here the outerfunction holds value num1=2 for every call of innerfunction
'''
x3 = outerFunction(3) #now this will atach value 3 with the innerfunction
print(x3(10))   #num2 will be 10 and num1 = 3

print(x3(20))  #num2 will be 20 and num1 = 3

print(outerFunction(3)(20))
