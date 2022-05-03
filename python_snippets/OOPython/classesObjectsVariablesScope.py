'''
Classes and object scope of variables and functions
'''
'''
***************************         Classes and object scope of variables
'''
class Test:
    staticVar1 = 10  # Static Variable
    staticVar2 = 102
    def __init__(self, initVar):
        self.instancVar1 = 20  # Instance Variable
        self.initVar1 = initVar
        print(self.staticVar1)
        self.staticVar1 = 100
        print(Test.staticVar1)
    def display(self):
        self.instancVar2 = 30
        print(self.staticVar1)
        print(Test.staticVar1)
t1 = Test(50)
t1.instanceVar3 = 40
print(t1.instancVar1, t1.instanceVar3, t1.staticVar1, Test.staticVar1)
t1.display()

t2 = Test(50)

#print(t2.instanceVar3) #Gives error as instance3 variable is not defined for t2 object of class Test

t1.staticVar1 = 20  # New instance Variable is created with name staticVar1

print(t1.instancVar1, t1.instanceVar3, t1.staticVar1, Test.staticVar1)

print(t2.staticVar1)

Test.staticVar1 = 1000  # Changed the value of static Variable

print(t1.staticVar1)
print(t2.staticVar1)
print(Test.staticVar2)
t1.staticVar2 = 103
# Test.staticVar2 = 103
print(t1.staticVar2)
print(t2.staticVar2)
print(Test.staticVar2)

'''
***************************         Classes and object scope of Functions
'''

class A :
    count =0  # static variable
    def __init__(self,a1,a2): #a1,a2 -- local variables to the A's constructor
        self.var1 = a1 # public Scope - instance varibale
        self.var2 = a2
        self._provar = 10 #protected scope -  will be accesible to same class and it's child classes
        self.__privar = 10  # private scope -- will be accessible to only and only same class

    def afunction(self):
        print('inside A function')

    def afunctionx(self):
        print('inside Ax function')

    def afuncttionY(self):
        print('inside Ay')


class B (A):
    def __init__(self,b1,b2,b3):
         super().__init__(b1,b2)
         self.var3 = b3

    def afunction(self):
        print('inside B function')

    def callSuperMethod(self):
        super().afunction()
        print("also inside B")

    def bfunctionx(self):
        print('inside Bx function')


class C(A):
    def __init__(self,c1,c2,c3,c4):
         super().__init__(c1,c2)
         self.var4 = c3
         self.var5 = c4

    def afunction(self):
        print('inside C function')

    def cfunctionx(self):
        print('inside Cx function')


a1 = A('a1','a2')
b1 = B('ba1','ba2','bvar')
c1 = C('ca1','ca2','cvar1','cvar2')
print(a1.__dict__)
print(b1.__dict__)
print(c1.__dict__)
a1.afunction() # A
a1.afunctionx() # Ax
a1.afuncttionY() #Ay

b1.afunction() #B
b1.callSuperMethod() # A
b1.bfunctionx()#Bx
b1.afuncttionY() #Ay

c1.afunction() #C
c1.cfunctionx()#Cx
c1.afuncttionY() #Ay



# firstcheck the method in runtime object -- if present call that method

# or else call parent class method (Except private)



# if method is overrriden and you want to call parents method

#with child object then you can add new method in child class which

#internally gives a call to parent method with super().





# super(). -- immediate parent member fileds --- method+ var

# super().__init__ -- immediate parent constructor calling


#???????? Private and Protected is denoted by underscore but it doesnt follow the rules as in java or other languages

#for java the meaning of variables is as follows
# protected variables : denoted by single underscore and accesible inside a same class or all it's child classes

# private variables : denoted by double underscore and accesible inside only inside same class, not accessible outside the class let it be child or nonchild

#Public Varibles -- by defulat every variable is public

#Local -- varibles whose scope is inside the method/constructor

#static -- These types of variables should be accesible by class name instead of object
