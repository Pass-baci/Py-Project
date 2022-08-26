#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import logging
import os
import pickle
from io import StringIO, BytesIO


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def main():
    # 读写文件操作
    try:
        f = open('./01data_type.py', 'r', encoding='gbk', errors='ignore')
        print(f.read())
    except IOError as e:
        logging.error(e)
    finally:
        if f:
            f.close()

    with open('./01data_type.py', 'r', errors='ignore') as f:
        # print(f.read())
        for line in f.readlines():
            print(line.strip())

    # StringIO
    s = StringIO()
    s.write('hello')
    s.write(' ')
    s.write('world')
    print(s.getvalue())

    s1 = StringIO('Hello!\nHi!\nGoodbye!')
    while True:
        temp = s1.readline()
        if temp == '':
            break
        print(temp.strip())

    # BytesIO
    b = BytesIO()
    b.write('中文'.encode('utf-8'))
    print(b.getvalue())

    b1 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
    print(b1.read().decode('utf-8'))

    # 操作文件与目录
    print(os.name)  # 操作系统类型
    print(os.environ)
    print(os.environ.get('GOPATH'))

    print(os.path.abspath('.'))
    print(os.path.join('/Users/michael', 'testdir'))

    # 字节序列化
    d = dict(name='Bob', age=20, score=88)
    print(pickle.dumps(d))
    b2 = pickle.dumps(d)
    print(pickle.loads(b2))

    # json序列化
    d = dict(name='Bob', age=20, score=88)
    print(json.dumps(d))
    j = json.dumps(d)
    print(json.loads(j))

    print(json.dumps(Student('Tom', 18, 99), default=student2dict))
    print(json.dumps(Student('Tom', 18, 99), default=lambda obj: obj.__dict__))


main()
