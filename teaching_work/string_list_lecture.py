Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s1 = " my name is ABCD "
>>> type(s1)
<class 'str'>
>>> s1[1]
'm'
>>> s1[-5:-1]
'ABCD'
>>> dir(s1)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> s1.islower()
False
>>> help(islower())
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    help(islower())
NameError: name 'islower' is not defined
>>> help(s1.islower())

>>> help(s1.islower)
Help on built-in function islower:

islower() method of builtins.str instance
    Return True if the string is a lowercase string, False otherwise.
    
    A string is lowercase if all cased characters in the string are lowercase and
    there is at least one cased character in the string.

>>> dir(s1)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> s1.capitalize()
' my name is abcd '
>>> help(s1.capitalize)
Help on built-in function capitalize:

capitalize() method of builtins.str instance
    Return a capitalized version of the string.
    
    More specifically, make the first character have upper case and the rest lower
    case.

>>> s2 = "my name is ABCD"
>>> s2.capitalize()
'My name is abcd'
>>> s2.uppercase()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s2.uppercase()
AttributeError: 'str' object has no attribute 'uppercase'
>>> s2.upper()
'MY NAME IS ABCD'
>>> s1.isdigit()
False
>>> dir(s1)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> s1.strip()
'my name is ABCD'
>>> s1
' my name is ABCD '
>>> s3 = s1.strip()
>>> s3
'my name is ABCD'
>>> s4 = '''
asjhjf
hskjhfksf
jhkjfwe'''
>>> s4
'\nasjhjf\nhskjhfksf\njhkjfwe'
>>> s4.lstrip()
'asjhjf\nhskjhfksf\njhkjfwe'
>>> s4.lstrip("\n")
'asjhjf\nhskjhfksf\njhkjfwe'
>>> s1.strip("\n")
' my name is ABCD '
>>> s4.replace("\n", " ")
' asjhjf hskjhfksf jhkjfwe'
>>> s1.count('a')
1
>>> s1
' my name is ABCD '
>>> s1.count('m')
2
>>> s1.count('z')
0
>>> s1.count('na')
1
>>> s1.find('abcd')
-1
>>> s1.find('ABCD')
12
>>> s1.split()
['my', 'name', 'is', 'ABCD']
>>> s1.split('m')
[' ', 'y na', 'e is ABCD ']
>>> l1 = s1.split()
>>> l1
['my', 'name', 'is', 'ABCD']
>>> " ".join(l1)
'my name is ABCD'
>>> ",".join(l1)
'my,name,is,ABCD'
>>> help(s1.translate)
Help on built-in function translate:

translate(table, /) method of builtins.str instance
    Replace each character in the string using the given translation table.
    
      table
        Translation table, which must be a mapping of Unicode ordinals to
        Unicode ordinals, strings, or None.
    
    The table must implement lookup/indexing via __getitem__, for instance a
    dictionary or list.  If this operation raises LookupError, the character is
    left untouched.  Characters mapped to None are deleted.

>>> s1.translate('a')
' my name is ABCD '
>>> 
>>> s1.index("my")
1
>>> s1.index("myt")
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    s1.index("myt")
ValueError: substring not found
>>> dir(s1)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(s1.split)
Help on built-in function split:

split(sep=None, maxsplit=-1) method of builtins.str instance
    Return a list of the words in the string, using sep as the delimiter string.
    
    sep
      The delimiter according which to split the string.
      None (the default value) means split according to any whitespace,
      and discard empty strings from the result.
    maxsplit
      Maximum number of splits to do.
      -1 (the default value) means no limit.

>>> l1=['a', 'b', 2, 3, 5, 'z']
>>> l1
['a', 'b', 2, 3, 5, 'z']
>>> l1[0]
'a'
>>> l1[0:1]
['a']
>>> l1[0:2]
['a', 'b']
>>> l1[-2:]
[5, 'z']
>>> l1[-1:-5:-1]
['z', 5, 3, 2]
>>> l1[-1:1:-1]
['z', 5, 3, 2]
>>> l1[:1:-1]
['z', 5, 3, 2]
>>> dir(l1)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> l1
['a', 'b', 2, 3, 5, 'z']
>>> l1.append("ABCD")
>>> l1
['a', 'b', 2, 3, 5, 'z', 'ABCD']
>>> l1.append("PQR")
>>> s1
' my name is ABCD '
>>> s1[1]
'm'
>>> s1[1]=z
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    s1[1]=z
NameError: name 'z' is not defined
>>> s1[1]='z'
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s1[1]='z'
TypeError: 'str' object does not support item assignment
>>> l1
['a', 'b', 2, 3, 5, 'z', 'ABCD', 'PQR']
>>> l1[1]
'b'
>>> l1[1] = 'c'
>>> l1
['a', 'c', 2, 3, 5, 'z', 'ABCD', 'PQR']
>>> help(l1.append)
Help on built-in function append:

append(object, /) method of builtins.list instance
    Append object to the end of the list.

>>> l2 = l1.copy()
>>> l2
['a', 'c', 2, 3, 5, 'z', 'ABCD', 'PQR']
>>> l2.clear()
>>> l2
[]
>>> l1
['a', 'c', 2, 3, 5, 'z', 'ABCD', 'PQR']
>>> l2=l1
>>> l2
['a', 'c', 2, 3, 5, 'z', 'ABCD', 'PQR']
>>> l1.count('a')
1
>>> l1.count('A')
0
>>> l1[-2]
'ABCD'
>>> l1[-2].count('A')
1
>>> l1
['a', 'c', 2, 3, 5, 'z', 'ABCD', 'PQR']
>>> l2 = [7, 8, 9]
>>> l2
[7, 8, 9]
>>> l1.append(l2)
>>> l1
['a', 'c', 2, 3, 5, 'z', 'ABCD', 'PQR', [7, 8, 9]]
>>> l1[-1]
[7, 8, 9]
>>> l1.extend(l2)
>>> l1
['a', 'c', 2, 3, 5, 'z', 'ABCD', 'PQR', [7, 8, 9], 7, 8, 9]
>>> l1[-1]
9
>>> l1 + l2
['a', 'c', 2, 3, 5, 'z', 'ABCD', 'PQR', [7, 8, 9], 7, 8, 9, 7, 8, 9]
>>> l1
['a', 'c', 2, 3, 5, 'z', 'ABCD', 'PQR', [7, 8, 9], 7, 8, 9]
>>> l1[-4]
[7, 8, 9]
>>> l1[-4][-1]
9
>>> l1[-4][0]
7
>>> l3 = [3,5]
>>> l1[-4].extend(l3)
>>> l1
['a', 'c', 2, 3, 5, 'z', 'ABCD', 'PQR', [7, 8, 9, 3, 5], 7, 8, 9]
>>> l1[-4].append(l3)
>>> l1
['a', 'c', 2, 3, 5, 'z', 'ABCD', 'PQR', [7, 8, 9, 3, 5, [3, 5]], 7, 8, 9]
>>> l1[-4][-1][-1]
5
>>> l1[-4][-1][0]
3
>>> l1.insert('b')
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    l1.insert('b')
TypeError: insert() takes exactly 2 arguments (1 given)
>>> l1.insert('b', 1)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    l1.insert('b', 1)
TypeError: 'str' object cannot be interpreted as an integer
>>> l1.insert(1, 'b')
>>> l1
['a', 'b', 'c', 2, 3, 5, 'z', 'ABCD', 'PQR', [7, 8, 9, 3, 5, [3, 5]], 7, 8, 9]
>>> l1.pop()
9
>>> l1.pop(0)
'a'
>>> l1
['b', 'c', 2, 3, 5, 'z', 'ABCD', 'PQR', [7, 8, 9, 3, 5, [3, 5]], 7, 8]
>>> l1.pop(-3)
[7, 8, 9, 3, 5, [3, 5]]
>>> l1
['b', 'c', 2, 3, 5, 'z', 'ABCD', 'PQR', 7, 8]
>>> l1.remove('ABCD')
>>> l1
['b', 'c', 2, 3, 5, 'z', 'PQR', 7, 8]
>>> l1.sort()
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    l1.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> l5 = [3,2,8,4,5]
>>> l5.sort()
>>> l5
[2, 3, 4, 5, 8]
>>> l5 = [3,2,8,4,5]
>>> sorted(l5)
[2, 3, 4, 5, 8]
>>> l5
[3, 2, 8, 4, 5]
>>> l5.reverse()
>>> l5
[5, 4, 8, 2, 3]
>>> l5.sort(reverse = True)
>>> l5
[8, 5, 4, 3, 2]
>>> 
