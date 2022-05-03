class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount
        self.display()

    def withdraw(self, amount):
        self.balance -= amount

    def display(self):
        print(f"Acoount balance of {self.name} is {self.balance}")

    def __gt__(self, other):
        return self.balance > other.balance

class SpclCustomer(Customer):

    def __init__(self, name, balance):
        super().__init__(name, balance)

    def deposite(self, amount):
        super().deposite(amount)
        self.balance +=2

c1 = Customer('Ram', 5000)
c2 = Customer('Deepak', 25000)

#print(c1 > c2)
#print(c1.__gt__(c2))
s2 = SpclCustomer('raj', 50000)
s2.deposite(1000)
c1.deposite(1000)
print(s2.balance)




