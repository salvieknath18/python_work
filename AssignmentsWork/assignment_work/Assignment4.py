n = input("Enter the number")

# Reverse the number
print("Reverse of number is : ", n[-1::-1])

# No is Palindrome or not
if n[:] == n[-1::-1]:
    print("No. is Palindrome")
else:
    print("No. is Not a Palindrome")

# count the frequency of digits in a number
list1 = list(set(n))
for i in range(len(list1)):
        print("Repetition of digit %s is %r" % (list1[i], n.count(list1[i], 0, len(n))))

# Power of each no
list2 = list(n)
for i in range(len(list2)):
    print("Power of %s is : %d" % (list2[i], (int(list2[i])) ** 2))

# Print ASCII values
for i in range(32, 123, 1):
    print("ASCII of %r is %r" % (chr(i), i))



