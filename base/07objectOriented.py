#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum, unique
from types import MethodType


class Student(object):
    __slots__ = ('name', 'age', 'set_age')


def set_age(self, age):
    self.age = age


class Student1(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width


class Student2(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    def __getattr__(self, attr):
        if attr == 'score':
            return 99

    def __call__(self):
        print('My name is %s.' % self.name)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


class Gender(Enum):
    Male = 0
    Female = 1


class Student3(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


def fn(self, name='world'):
    print('hello, %s' % name)


if __name__ == '__main__':
    # __slots__[限制该class实例的属性，方法]
    s = Student()
    s.name = 'Michael'
    print(s.name)

    s.set_age = MethodType(set_age, s)  # [可以给该实例绑定任何属性和方法]
    s.set_age(25)
    print(s.age)

    # @property
    # @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
    s1 = Student1()
    s1.score = 99
    print(s1.score)

    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')
    # 多重继承
    # 定制类
    s2 = Student2('baci')
    print(s2)
    for n in Fib():
        print(n)
    print(Fib()[5])
    print(s2.score)
    print(Chain().status.user.timeline.list)
    s2()
    print(callable(s2))

    # 枚举
    Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)
    print(Weekday.Mon)
    print(Weekday.Mon.value)

    # 元类
    # 通过type来创建类
    Hello = type('Hello', (object,), dict(hello=fn))
    h = Hello()
    h.hello()
    h.hello('baci')
