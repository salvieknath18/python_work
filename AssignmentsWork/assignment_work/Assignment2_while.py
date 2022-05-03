n = input("Enter a number")

#Sum of natural numbers up to n
i=1
sum = 0
while i <= n:
    sum += i
    i += 1
print sum
print "Sum of numbers:",sum

#Sum of natural numbers up to n without variable i
sum = 0
while n > 0:
    sum += n
    n -= 1
print sum
print "Sum of numbers:",sum

#Sum even numbers from 1 to n
i=1
sum = 0
while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1
print "Sum of Even numbers:",sum

#Sum even numbers from 1 to n
i=1
sum = 0
while i <= n:
    if i % 2 == 1:
        sum += i
    i += 1
print "Sum of odd numbers:",sum

#Product of number
i = 1
prod = 1
while i<=n:
    prod *= i
    i+=1
print "Product of n number",prod

#multiplication table of any number
i = 1
while i<=10:
    print i * n , 
    i+=1

#Count number of digits in number
m = input("enter a number to count digits")
print "Number of digits",len(str(m))

count = 1
while m / 10 != 0:
    count +=1
    m /= 10
print "number of digits :", count
        


