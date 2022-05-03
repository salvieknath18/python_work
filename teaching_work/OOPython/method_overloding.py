class A():
    def f1(self):
        print("A: f1")

class B(A):
    def f1(self):
        super().f1()
        print("B: f1")

b = B()
b.f1()
