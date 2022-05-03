string = 'python'
listobj = [var for var in string]
print listobj

employee = {"Name":"Jatin", "Age":33, "Location": "Pune"}
listobj = [var for var in employee]
print listobj

listobj = [employee[var] for var in employee]
print listobj

listoflist = [[1, 2], [3, 4], [5, 6]]
listobj = [j for i in listoflist for j in i]
print listobj
listobj = [j for i in listoflist for j in i if j % 2 == 0]
print listobj


notaprime = {j for i in range(2, 9) for j in range(1*2, 100, 1)}
prime = [i for i in range(2,100) if i not in notaprime]

list1 = ['Jatin', 'Rahul', 'Mohit']
dictobj = {i:list1[i] for i in range(len(list1))} 
print dictobj
dictobj = {i:j for i,j in enumerate(list1)}
print dictobj


list1 = ['Jatin', 'Rahul', 'Mohit']
list2 = ['Mighlani', 'Gandhi', 'Chauhan']
dictobj1 = {list2[i]:list1[i] for i in range(len(list1))}
print dictobj1
dictobj2 = {list1[i]+" "+list2[i] for i in range(len(list1))}
print dictobj2
dictobj1 = {list2[i]:list1[i] for i, j in enumerate(list1)}
print dictobj1

