class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __eq__(self, other):
        return self.marks == other.marks

    def __str__(self):
        return f"Student {self.name} has marks {self.marks}"

s1 = Student('ABC', 46)
s2 = Student('PQR', 46)
s3 = Student('XYZ', 55)

print(s1>s2)
if s1 == s2:
    print("same scholars")
print(s1)

class sp_student(Student):

    def __init__(self, name, marks, rank):
        super().__init__(name, marks)
        self.rank = rank

sp4 = sp_student('RTYUIOP', 100, 1)
print(sp4.name)
print(sp4 > s1)
