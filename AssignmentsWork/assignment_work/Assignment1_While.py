n = input("Enter the input")

#printing the number
i=1;
while i<=n :
    print i,
    i +=1
print "done"

#printing n natural numbers in reverse way
while n>1:
    print n,
    n -=1
print "done"

#printing n natural numbers in reverse way
i=1
while i<=n:
    print n-i+1,
    i +=1
print "done"

#print character from a to z
i=97
while i < (97 + 26):
    print chr(i),
    i +=1
print "done"

#print even numbers between 1 to 100
i=0
while i<=100:
    if i % 2 == 0:
        print i,
    i +=1
print "done"

#print odd numbers between 1 to 100
i=0
while i<=100:
    if i % 2 == 1:
        print i,
    i +=1
print "done"
