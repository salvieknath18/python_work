'''
iterators
'''
'''
if a class has __itr__ and __next__ method the class is iterator class
and the object is iterative object
'''

'''
********************************       List is a iterator
list has inbuit itr and next methods
'''
list1 = [i for i in range(101)]# created a list
'''
iteritem = iter(list1)
print(next(iteritem))
print(next(iteritem))
while iteritem:
    print(next(iteritem))  #iterat values up to last object
#print(next(iteritem))  #this line will give error at next method as iterations are completed

'''
'''***************************         Creating our own iterator'''

class DemoIterator():

    index = 0

    def __init__(self,number):
        self.value = number

    def __iter__(self):
        return self

    def __next__(self):
        if DemoIterator.index < self.value:
            DemoIterator.index += 2
            return DemoIterator.index
        else:
            #try:
            raise StopIteration
            #except Exception as E:
                #print("Iterations are over")

for ele in DemoIterator(10):
    print(ele)

'''
d = DemoIterator(10)
print(d.__next__())  # print next value for number 10(logic in __next__ method) this will be 20

iterator_d = d.__iter__()# we can call next method for __iter__() object from above statement
print(next(iterator_d))#next value for number 10(this will be 40
print(iterator_d)

for item in DemoIterator(20):
    print(item)
'''
