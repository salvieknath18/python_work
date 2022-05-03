'''
print(values objects,seperator, end, file, buffer)
'''
print(1,2,3) #1 2 3

print('Eknayth', 123, 'hiii', 1234)     #Eknayth 123 hiii 1234
print('Eknayth', 123, 'hiii', 1234,sep='__', end='$$$')    #Eknayth__123__hiii__1234$$$
a=5
print("The Value is : ", a)   #The Value is :  5
b=10
c="Hiii"
print("The Value is: %d and the second value is: %d and the string is %s" %(a,b,c))
    #The Value is: 5 and the second value is: 10 and the string is Hiii
print("The Value is: {} and the second value is: {} and the string is {}".format(a,b,c))
   #The Value is: 5 and the second value is: 10 and the string is Hiii
print("The Value is: {2} and the second value is: {1} and the string is {0}".format(a,b,c))
   #The Value is: Hiii and the second value is: 10 and the string is 5
print("The Value is: {val1} and the second value is: {val2} and the string is {str1}".format(val1=a,val2=b,str1=c))
   #The Value is: 5 and the second value is: 10 and the string is Hiii
x=1234.1234567
print("The Value of x is %f"%x)
   #The Value of x is 1234.123457
print("The Value of x is %1.1f"%x)
   #The Value of x is 1234.1
print("The Value of x is %2.2f"%x)
   #The Value of x is 1234.12
print("The Value of x is %3.3f"%x)
   #The Value of x is 1234.123

s1 = "ABCD"
s1.find('B')
