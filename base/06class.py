#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    pass


class Student1(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


class Student2(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Student3(object):
    name = 'Student3'


if __name__ == '__main__':
    s = Student()
    s.Name = 'baci'
    print(s.Name)

    s1 = Student1('baci', 200)
    print(s1.name, s1.score)
    s1.print_score()
    print(s1.get_grade())

    # __xxx__【特殊变量】
    # __xxx【私有变量】
    # _xxx【视为私有变量，不能随意访问】
    s2 = Student1('baci', 300)
    s1.print_score()

    # 继承和多态
    dog = Dog()
    dog.run()
    cat = Cat()
    cat.run()

    # 获取对象信息
    print(type(123))
    print(dir(s2))
    print(hasattr(s2, 'x'))
    setattr(s2, 'age', 18)
    print(hasattr(s2, 'age'))
    print(s2.age)

    # 实例属性和类属性[不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，
    # 但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性]
    s3 = Student3()
    print(s3.name)

