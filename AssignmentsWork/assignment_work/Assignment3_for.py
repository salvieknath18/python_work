n = input("Enter a number")

print str(n)[0],str(n)[-1]

print int(str(n)[0]) + int(str(n)[-1])

print str(n)[-1] + str(n)[1:-1] + str(n)[0]

sum = 0
for i in range(len(str(n))):
    sum += int(str(n)[i])
print "sum of intergers : ", sum

prod = 1
for i in range(len(str(n))):
    prod *= int(str(n)[i])
print "sum of intergers : ", prod
