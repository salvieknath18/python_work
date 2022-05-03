list1 = ['Jatin', 'Rahul', 'Mohit']
dictobj = {i:list1[i] for i in range(len(list1))} 
print dictobj

list1 = ['Jatin', 'Rahul', 'Mohit']
list2 = ['Mighlani', 'Gandhi', 'Chauhan']
dictobj1 = {list2[i]:list1[i] for i in range(len(list1))}
print dictobj1
dictobj2 = {list1[i]+" "+list2[i] for i in range(len(list1))}
print dictobj2


for i in range(11):
    print " " * (11-i) + " *" * i
    

for i in range(11):
    print " " * (11-i-1) + " *" * i
for i in range(9):
    print " "+" " * (i) + " *" * (9-i)

for i in range(1,11,2):
    print " " * (11-(i+1)/2) + "*" * i
