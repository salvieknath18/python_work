from abc import ABC, abstractmethod

class IBank(ABC):

    def __init__(self, name):
        self.bankName = name

    @abstractmethod
    def deposite(self): pass

    @abstractmethod
    def credit(self): pass

class SBI(IBank):

    def __init__(self, name, city):
        super().__init__(name)
        self.city = city

    def deposite(self):
        print("deposite started")

    def credit(self):
        print("credit started")

class HDFC(IBank):

    def __init__(self, name, state):
        super().__init__(name)
        self.state = state

    def deposite(self):
        print("deposite of HDFC started")

    def credit(self):
        print("credit of HDFC started")

sbi = SBI('SBI Bank','Mumbai')
hdfc = HDFC('SBI Bank','Gujrat')

sbi.deposite()
hdfc.credit()

