# coding:utf-8

def make_iter():
    for i in range(10):
        yield i


if __name__ == '__main__':
    iter_obj = iter((1, 2, 3))
    # print(next(iter_obj))
    # print(next(iter_obj))
    # print(next(iter_obj))

    for i in iter_obj:
        print(i)

    for i in make_iter():
        print(i)

    iter_obj1 = (i for i in range(10))

    for i in iter_obj1:
        print(i)
