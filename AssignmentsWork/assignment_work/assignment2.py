n = int(input("Enter number n : "))
sum1 = 0

# Printing sum of n natural numbers
for i in range(n+1):
    sum1 += i
print(sum1)

# Direct function
sum2 = sum(range(1, n+1, 1))
print(sum2)

# Printing sum of n even numbers
sum2 = sum(range(0, n+1, 2))
print(sum2)

# Printing sum of n odd numbers
sum2 = sum(range(1, n+1, 2))
print(sum2)

# multiplication table of any number
for i in range(n, n * 10 + 1, n):
    print(i)

# count number of digits in number
NOD = len(str(n))
print(NOD)

