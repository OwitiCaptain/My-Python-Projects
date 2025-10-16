def add_student():

    Student.name = input("Enter student name: ")
    Student.course = input("Enter student course: ")

    students.append(Student.name)
    print(f"{Student.name} was registered to {Student.course} successfully")
    return students

while True:
    students = []
    student = Student.name
    class Student:
        def __init__(self,name,course):
            self.name = name
            self.course = course

    add_student()
    print(list(students))
    students.append(student)
    
