from store.store import students
from comm_error.comm_error import CommError
from model.student import Student
import random

def getStudentById(student_id):
    for student in students:
        if student.id == student_id:
            return student
    raise CommError(100, "No fund Student")

def getStudentList():
    return students

def createStudent(name, age, lang='中文'):
    student = Student(random.randint(1, 10000), name, age, lang)
    students.append(student)

def updateStudent(student):
    for value in students:
        if value.id == student.id:
            value = student