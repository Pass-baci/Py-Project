#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


# 定义函数时，需要确定函数名和参数个数；

# 如果有必要，可以先对参数的数据类型做检查；

# 函数体内部可以用return随时返回函数结果；

# 函数执行完毕也没有return语句时，自动return None。

# 函数可以同时返回多个值，但其实就是一个tuple。


# 定义一个函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 空函数
def nop():
    pass


# 多返回值,原来返回值是一个tuple
def move(x, y, step, angle=1.0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0的两个解。
def quadratic(a, b, c):
    if not isinstance(a * b * c, (int, float)):
        raise TypeError('bad operand type')
    q = b * b - 4 * a * c
    if q < 0:
        print('此方程无解')
    elif q == 0:
        print('此方程解唯一')
        x = (-b) / (2 * a)
        return x
    else:
        x1 = ((-b + math.sqrt(q)) / (2 * a))
        x2 = ((-b - math.sqrt(q)) / (2 * a))
        return x1, x2


# 参数默认值
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 参数多个默认值
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


# 参数默认值为None
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 参数可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


def person1(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


def mul(*args):
    if len(args) == 0:
        raise TypeError('Len Error')
    sum = 1
    for num in args:
        if isinstance(num, (int, float)):
            sum *= num
        else:
            raise TypeError('Type Error')
    return sum


if __name__ == '__main__':
    print(my_abs(-10))
    print(nop())
    print(move(100, 100, 60, math.pi / 6))
    if quadratic(2, 3, 1) != (-0.5, -1.0):
        print('测试失败')
    elif quadratic(1, 3, -4) != (1.0, -4.0):
        print('测试失败')
    else:
        print('测试成功')
    print(power(5))
    enroll('Sarah', 'F')
    enroll('Bob', 'M', 7)
    enroll('Adam', 'M', city='Tianjin')
    print(add_end())
    print(add_end())
    print(calc())
    print(calc(1, 2))
    person('Michael', 30)
    person('Bob', 35, city='Beijing')
    person('Adam', 45, gender='M', job='Engineer')
    extra = {'city': 'Beijing', 'job': 'Engineer'}
    person('Jack', 24, city=extra['city'], job=extra['job'])
    person('Jack', 24, **extra)
    person1('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
    person('Jack', 24, city='Beijing', job='Engineer')
    f1(1, 2)
    f1(1, 2, c=3)
    f1(1, 2, 3, 'a', 'b')
    f1(1, 2, 3, 'a', 'b', x=99)
    f2(1, 2, d=99, ext=None)
    print(mul(1, 1, 2, 3, 4, 5, 6, 7))
    print(fact(100))
