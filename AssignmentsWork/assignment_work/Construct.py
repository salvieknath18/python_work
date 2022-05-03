students = []


class Student:
    def __init__(self, name, student_id=11):
        student = {"name": name, "student_id": student_id}
        students.append(student)

    def __str__(self):
        return "Student"


mark = Student("Eknath")
## student = Student("Eknath")
print(mark)
