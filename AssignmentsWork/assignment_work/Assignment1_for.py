n=input("enter number")
for i in range(n):
    print i+1,
print "done"

for i in range(n):
     print n-i,
print "done"
    
for i in range(n,0,-1): #Reverse indexing
     print i,
print "done"

for i in range(97, 97+26):
    print chr(i),
print "done"

for i in range(0, n+1, 2):
    print i,
print "done"

for i in range(1, n+1, 2):
    print i,
print "done"

sum=0
for i in range(n+1):
    sum += i
print "Sum is : ", sum

sum=0
for i in range(0,n+1,2):
    sum += i
print "Sum is even: ", sum

sum=0
for i in range(1,n+1,2):
    sum += i
print "Sum is odd: ", sum

for i in range(1,11):
    print i * n,
print "done"

print len(str(n))
