Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list1 = [1, 1, 2, 3, 4, 5, 5]
>>> map(lambda x:x if list1.count(x)>1, list(set(list1))
    
SyntaxError: invalid syntax
>>> map(lambda x:x if list1.count(x)>1, list(set(list1)))
SyntaxError: invalid syntax
>>> map(lambda x:x if list1.count(x)>1 else 0, list(set(list1)))
[1, 0, 0, 0, 5]
>>> map(lambda x:x if list1.count(x)=1 else 0, list(set(list1)))
SyntaxError: invalid syntax
>>> map(lambda x:x if list1.count(x)=1 else 0, list(set(list1)))
SyntaxError: invalid syntax
>>> map(lambda x:x if list1.count(x)== 1 else 0, list(set(list1)))
[0, 2, 3, 4, 0]
>>> 
