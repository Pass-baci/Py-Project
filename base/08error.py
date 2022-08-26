#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from functools import reduce


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

def bar1():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise


def str2num(s):
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)



# def main():
    # try:
    #     bar('0')
    # except Exception as e:
    #     logging.exception(e)
    # finally:
    #     print('finally...')
    #
    # foo('0')

    # bar1()


main()

# if __name__ == '__main__':
#     try:
#         print('try....')
#         # r = 10 / 0
#         r = 10 / 2
#         print('result:', r)
#     except ZeroDivisionError as e:
#         print('except:', e)
#     finally:
#         print('finally...')
#     print('End')
