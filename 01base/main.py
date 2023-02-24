# coding:utf-8
import os


class NewError(Exception):
    def __init__(self, message):
        self.message = message


class NewError1(Exception):
    def __init__(self, message):
        self.message = message


def test1(msg):
    raise NewError(msg)


def test2(msg):
    raise NewError1(msg)


if __name__ == '__main__':
    try:
        # test1('test1 error')
        test2('test2 error')
    except (NewError, NewError1) as e:
        print(e)
    finally:
        print('finally')
