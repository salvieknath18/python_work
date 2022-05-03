# Take a number
n = int(input("Enter a number"))

# Fetching first and last digit
print("first digit is", int(str(n)[0]))
print("Last digit is", int(str(n)[-1]))
print("Sum is : ", int(str(n)[0])+int(str(n)[-1]))

# Swap first and last digits
strNum = str(n)
print("swapped last and first digits : ", int(strNum[-1] + strNum[1:-1:1] + strNum[0]))

# Sum of digits of a number
sum1 = 0
for i in range(len(strNum)):
    sum1 += int(strNum[i])
print("Sum of Digits is : ", sum1)

# Product of digits of a number
prod1 = 1
for i in range(len(strNum)):
    prod1 *= int(strNum[i])
print("Sum of Digits is : ", prod1)


