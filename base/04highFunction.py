#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools
import time
from functools import reduce


def add1(x, y, f):
    return f(x) + f(y)


def f(x):
    return x * x


def add(x, y):
    return x + y


def fn(x, y):
    return x * 10 + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


def is_odd(n):
    return n % 2 == 1


def not_empty(s):
    return s and s.strip()


def lazy_sum(*args):
    def sum1():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum1


def inc():
    x = 0

    def fn():
        nonlocal x
        x = x + 1
        return x

    return fn


def createCounter():
    x = 0

    def counter():
        nonlocal x
        x = x + 1
        return x

    return counter


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-3-25')


def metric(fn):
    # @functools.wraps(fn)
    def wrapper(*args, **key):
        t = time.time()
        f = fn(*args, **key)
        print('%s executed in %s ms' % (fn.__name__, time.time() - t))
        return f
    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


if __name__ == '__main__':
    # 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
    print(add1(2, -2, abs))

    # map()和reduce()
    r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(list(r))
    print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
    print(reduce(add, [1, 3, 5, 7, 9]))
    print(list(map(char2num, '13579')))
    print(reduce(fn, map(char2num, '13579')))

    # filter[和map()类似，filter()也接收一个函数和一个序列。
    # 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。]
    print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
    print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

    # sorted
    print(sorted([36, 5, -12, 9, -21]))
    print(sorted([36, 5, -12, 9, -21], key=abs))
    print(sorted(['bob', 'about', 'Zoo', 'Credit']))

    # 返回函数
    f1 = lazy_sum(1, 2, 3, 4, 5)
    print(f1())

    # nonlocal
    print(inc()())
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')

    # 匿名函数[Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。]
    f = lambda x: x + 1
    print(f(1))
    L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
    print(L)

    # 装饰器[把@log放到now()函数的定义处，相当于执行了语句：now = log(now)]
    now()
    f = fast(11, 22)
    s = slow(11, 22, 33)
    print(f, s)
    if f != 33:
        print('测试失败!')
    elif s != 7986:
        print('测试失败!')
    else:
        print('测试成功!')

    # 偏函数[functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单]
    print(int('123', 10))
    int2 = functools.partial(int, base=2)
    print(int2('1000000'))
