from repo.student_oper import *
from comm_error.comm_error import CommError

if __name__ == '__main__':
    for i in range(10):
        createStudent("Tom", i+10)
    students = getStudentList()
    for student in students:
        print(student.id, student.name, student.age, student.lang)

    try:
        student = getStudentById(12)
        print(student.id, student.name, student.age, student.lang)
    except CommError as e:
        print(f'查询错误信息{e}')