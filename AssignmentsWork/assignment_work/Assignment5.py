# Factorial
n = input("Enter Number")
fact = 1
for i in range(1, int(n)+1):
    fact *= i
print("Factorial of number %s is %d" % (n, fact))

# Prime Numbers from 1 to n
list1 = ['3']
cnt = 0
for i in range(4, int(n)+1):
    for j in range(2, i-1):
        if i % j == 0:
            cnt = 1
    if cnt == 0:
        list1.append(str(i))
    cnt = 0

print("Prime Numbers up to %r  %r " % (n, list1))


# Number is prime or not
cnt = 0
for i in range(2, int(int(n) / 2) + 1):
    if int(n) % i == 0:
        print("No is Not prime")
        cnt = 1
        break
if cnt == 0:
    print("No is Prime")


# HCF and LCM of Two Numbers
n1 = int(input("enter first number : "))
n2 = int(input("enter Second number : "))
minvalue = int(min(n1, n2))
HCF = 1
for i in (range(minvalue)):
    if n1 % (minvalue - i) == 0 and n2 % (minvalue - i) == 0:
        print("HCF is %r " % (minvalue-i))
        HCF = minvalue - i
        break

LCM = int((n1 * n2) / HCF)
print("LCM is %r " % LCM)
