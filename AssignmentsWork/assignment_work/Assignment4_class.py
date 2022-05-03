number  = raw_input("enter number")
count = dict()
for i in number :
    if i in count:
        count += 1
    else:
        count = 1

print count
