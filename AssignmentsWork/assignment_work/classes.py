students = []


class Student:
    def add_student(self, name, student_id=11):
        student1 = {"name": name, "student_id": student_id}
        students.append(student1)


student = Student()
student.add_student("Eknath")
print(students)
