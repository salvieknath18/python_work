'''
MRO in classes
'''

class a():
    def add(self,a,b):
        return a+b
'''
a = A()
A.add(a,3,4)
a.add(4,5)
'''
class b(a):
    pass

class c(a):
    pass

class d():
    pass

class e(b):
    pass

class f(c,d):
    pass

class g(e,f,d):
    pass


print(g.__mro__)
