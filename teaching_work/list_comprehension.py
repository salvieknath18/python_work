Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> input()
dfggh
'dfggh'
>>> input()
dfggh
SyntaxError: multiple statements found while compiling a single statement
>>> input()
sadsa
'sadsa'
>>> input("Enter a number")
Enter a number45
'45'
>>> int(input("Enter a number"))
Enter a number45
45
>>> print("hello")
hello
>>> 
============= RESTART: C:/Users/Eknath/Desktop/desktop_delete.py =============
i am ABCD city pune
>>> 
============= RESTART: C:/Users/Eknath/Desktop/desktop_delete.py =============
i am ABCD city pune
i am XYZ city mumbai
>>> 
============= RESTART: C:/Users/Eknath/Desktop/desktop_delete.py =============
i am ABCD;city pune
i am XYZ city mumbai
>>> 
============= RESTART: C:/Users/Eknath/Desktop/desktop_delete.py =============
i am ABCD;city pune
i am XYZ city mumbai
>>> 
============= RESTART: C:/Users/Eknath/Desktop/desktop_delete.py =============
i am ABCD;city punei am XYZ city mumbai
>>> 
============= RESTART: C:/Users/Eknath/Desktop/desktop_delete.py =============
i am ABCD;city punei am XYZ, city Mumbai
>>> 
============= RESTART: C:/Users/Eknath/Desktop/desktop_delete.py =============
i am XYZ, city Mumbai
>>> 
============= RESTART: C:/Users/Eknath/Desktop/desktop_delete.py =============
i am XYZ, city Mumbai
>>> 
============= RESTART: C:/Users/Eknath/Desktop/desktop_delete.py =============
[2, 6, 8]
>>> [e for e in [2,3,5,7,6,9,8] if e%2==0]
[2, 6, 8]
>>> l1 = [2,3,5,7,6,9,8]
>>> [e for e in l1]
[2, 3, 5, 7, 6, 9, 8]
>>> l2 = ['apple', 'chiku', 'banana', 'peru', 'watermelon']
>>> [f for f in l2 if 'a' in f]
['apple', 'banana', 'watermelon']
>>> [f for f in l2 if 'a' in f and 'c' in f]
[]
>>> [f for f in l2 if 'a' in f or 'c' in f]
['apple', 'chiku', 'banana', 'watermelon']
>>> [f.count('a') for f in l2]
[1, 0, 3, 0, 1]
>>> 
========= RESTART: D:\scodeen\pythondata\P6\looping_on_real_data.py =========
>>> [p['name'] for p in personDetails]
['John', 'chandu', 'ashok', 'akshay']
>>> [p['name'] for p in personDetails for c in p['cars'] if c['name']=='BMW']
['chandu', 'ashok', 'akshay']
>>> [c['models'] for p in personDetails for c in p['cars'] if c['name']=='BMW']
[['320', 'X3', 'X5'], ['320', 'X3', 'X5'], ['320', 'X3', 'X5']]
>>> l2 = [c['models'] for p in personDetails for c in p['cars'] if c['name']=='BMW']
>>> l2
[['320', 'X3', 'X5'], ['320', 'X3', 'X5'], ['320', 'X3', 'X5']]
>>> [[2,4],[3,7],[4,16],[5,24]]
[[2, 4], [3, 7], [4, 16], [5, 24]]
>>> l3 = [[2,4],[3,7],[4,16],[5,24]]
>>> [pair for pair in l3 if pair[1] == (pair[0]**2)]
[[2, 4], [4, 16]]
>>> [pair[0] for pair in l3 if pair[1] == (pair[0]**2)]
[2, 4]
>>> 
