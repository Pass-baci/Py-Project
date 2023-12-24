# coding=utf-8
import json

if __name__ == '__main__':
    a = dict(name='Tom', age=11)
    b = json.dumps(a)
    c = json.loads(b)
    print(b)
    print(c)
