from abc import ABC, abstractmethod

class bank(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def deposite(self):
        pass

class SBI(bank):

    def __init__(self):
        pass

    def deposite(self):
        pass

s = SBI()