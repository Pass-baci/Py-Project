# coding:utf-8
import functools

if __name__ == '__main__':
    str_list = ['abc', 'abd', 'dbr']
    res = filter(lambda x: 'a' in x, str_list)
    print(list(res))

    res1 = functools.reduce(lambda x, y: x+y, str_list)
    print(res1)

    res2 = map(lambda x: 'a' in x, str_list)
    print(list(res2))

