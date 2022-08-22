#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
from collections.abc import Iterable


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)


if __name__ == '__main__':
    # 切片
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    print(L[0:3], L[:3], L[:3], L[-2:])
    L = list(range(100))
    print(L)
    print(L[:10:2])
    print(L[::5])
    print((0, 1, 2, 3, 4, 5)[:3])
    print('ABCDEFG'[:3])

    # 迭代
    for i in L:
        print(i)

    # 列表生成器
    print(list(range(100)))
    print([x * x for x in range(1, 11)])
    print([x * x for x in range(1, 11) if x % 2 == 0])
    print([m + n for m in 'ABC' for n in 'XYZ'])
    print([d for d in os.listdir('.')])
    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    for k, v in d.items():
        print(k, v)
    print([k + '=' + v for k, v in d.items()])
    L = ['Hello', 'World', 'IBM', 'Apple']
    print([s.lower() for s in L])
    print([x for x in range(1, 20) if x % 2 == 0])
    print([x if x % 2 == 0 else 0 for x in range(1, 20)])
    L1 = ['Hello', 'World', 18, 'Apple', None]
    print([s.lower() for s in L1 if isinstance(s, str)])

    # 生成器generator[generator保存的是算法]
    L = [x * x for x in range(10)]
    print(L)
    g = (x * x for x in range(10))
    print(g)
    for n in g:
        print(n)
    f = fib(6)
    print(f)
    for n in f:
        print(n)
    o = odd()
    print(next(o))
    for o in odd():
        print(o)

    # 迭代器[可以直接作用于for循环的对象统称为可迭代对象：Iterable; 凡是可作用于next()函数的对象都是Iterator类型]
    print(isinstance([], Iterable))
    print(isinstance({}, Iterable))
    print(isinstance('abc', Iterable))
    print(isinstance((x for x in range(100)), Iterable))
    print(isinstance(100, Iterable))



