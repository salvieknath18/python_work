Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d1 = {'k1':'abc', 'k2':12345, 'k3':[1,3,5], 'k4':{1:'a',2:'b'}}
>>> d2 = {1:'a', 2:'b'}
>>> type(d2)
<class 'dict'>
>>> d2
{1: 'a', 2: 'b'}
>>> d2[1]
'a'
]
>>> d2[1]
'a'
>>> d1['k1']
'abc'
>>> d1[0]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    d1[0]
KeyError: 0
>>> d2[2]
'b'
>>> d2[2]='z'
>>> d2
{1: 'a', 2: 'z'}
>>> d3 = {'a':'A', 'b':'B'}
>>> d3
{'a': 'A', 'b': 'B'}
>>> d3['c']
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d3['c']
KeyError: 'c'
>>> d3['b']='Y'
>>> d3
{'a': 'A', 'b': 'Y'}
>>> d3['c']='Z'
>>> d3
{'a': 'A', 'b': 'Y', 'c': 'Z'}
>>> d2
{1: 'a', 2: 'z'}
>>> d2 = {'a': 'A', 'b': 'B', 'b':'C'}
>>> d2
{'a': 'A', 'b': 'C'}
>>> d2 = {'a': 'A', 'b': 'B', 'c':'B'}
>>> d2
{'a': 'A', 'b': 'B', 'c': 'B'}
>>> dir(d2)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> d2.keys()
dict_keys(['a', 'b', 'c'])
>>> d2.values()
dict_values(['A', 'B', 'B'])
>>> d2.items()
dict_items([('a', 'A'), ('b', 'B'), ('c', 'B')])
>>> d2.popitem()
('c', 'B')
>>> d2
{'a': 'A', 'b': 'B'}
>>> d2.pop('a')
'A'
>>> d2
{'b': 'B'}
>>> d2.popitem({'b':'B'})
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    d2.popitem({'b':'B'})
TypeError: popitem() takes no arguments (1 given)
>>> d2 = {'a': 'A', 'b': 'B', 'c':'B'}
>>> 
>>> d2['b']
'B'
>>> d2.get('b')
'B'
>>> d2.get('d')
>>> d2['d']
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    d2['d']
KeyError: 'd'
>>> d2.get('d', 'XYZ')
'XYZ'
>>> d2.get('b', 'XYZ')
'B'
>>> d2.copy
<built-in method copy of dict object at 0x00000070F0B15818>
>>> d3 = d2.copy()
>>> d3
{'a': 'A', 'b': 'B', 'c': 'B'}
>>> d2['b'] = "z"
>>> d2
{'a': 'A', 'b': 'z', 'c': 'B'}
>>> d3
{'a': 'A', 'b': 'B', 'c': 'B'}
>>> d4 = d3
>>> d3['b'] = 'X'
>>> d3
{'a': 'A', 'b': 'X', 'c': 'B'}
>>> d4
{'a': 'A', 'b': 'X', 'c': 'B'}
>>> d2['p']='P'
>>> d2
{'a': 'A', 'b': 'z', 'c': 'B', 'p': 'P'}
>>> d3
{'a': 'A', 'b': 'X', 'c': 'B'}
>>> d2.update(d3)
>>> d2
{'a': 'A', 'b': 'X', 'c': 'B', 'p': 'P'}
>>> d2.update({'d':"D", 'g':'G'})
>>> d2
{'a': 'A', 'b': 'X', 'c': 'B', 'p': 'P', 'd': 'D', 'g': 'G'}
>>> d3.clear()
>>> d3
{}
>>> a = 10
>>> type(a)
<class 'int'>
>>> dir(a)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> b = 10
>>> a
10
>>> b
10
>>> a == b
True
>>> a is b
True
>>> id(a)
140716353614368
>>> id(b)
140716353614368
>>> c = 300
>>> d=300
>>> c == d
True
>>> c is d
False
>>> id(c)
485076946128
>>> id(d)
485076946000
>>> c = 10
>>> id(c)
140716353614368
>>> f1 = 10.0
>>> type(f1)
<class 'float'>
>>> c1 = 3+4j
>>> type(c1)
<class 'complex'>
>>> c1
(3+4j)
>>> c1.real
3.0
>>> c1.imag
4.0
>>> b1 = True
>>> type(b1)
<class 'bool'>
>>> b1
True
>>> t1 = (2,3,4,5)
>>> dir(t1)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> t1[1]
3
>>> t1[1] = 5
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    t1[1] = 5
TypeError: 'tuple' object does not support item assignment
>>> range(5)
range(0, 5)
>>> r1 = range(0,5)
>>> type(r1)
<class 'range'>
>>> list(r1)
[0, 1, 2, 3, 4]
>>> list(range(0,5))
[0, 1, 2, 3, 4]
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(1,5))
[1, 2, 3, 4]
>>> list(range(0,100))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> list(range(0,100,2))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> list(range(1,100,2))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> 
