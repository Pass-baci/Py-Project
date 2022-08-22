#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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
