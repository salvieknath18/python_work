n = input("Enter a number")

# Armstrong number
sum1 = 0
prod = 1
for i in range(len(n)):
    prod = int(n[i]) ** 3
    sum1 += prod

if sum1 == int(n):
    print("Number %s is Armstrong number" % n)
else:
    print("Number %s is Not Armstrong number" % n)

# armstrong number up to n
list1 = ["Armstrong Numbers upto n"]
for j in range(int(n)+1):
    sum1 = 0
    prod = 1
    for i in range(len(str(j))):
        prod = int(str(j)[i]) ** 3
        sum1 += prod
    if sum1 == j:
        list1.append(str(j))
print(list1)

# Fibonacci series up to n
list1 = [1, 1]
for i in range(2, int(n)):
    list1.append(list1[i-2]+list1[i-1])
print(list1)

# Pascal Triangle up to np
list1 = [1]
np = input("Enter n for pascal triangle")
print(list1)
for i in range(int(np)-1):
    list2 = [1]
    for j in range(i):
        list2.append(list1[j] + list1[j+1])
    list1 = list2
    list1.append(1)
    print(list1)

