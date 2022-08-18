#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    print(123)  # 整数
    print('Tom')  # 字符串 默认Unicode编码
    print('\\')  # 转义
    print(r'\\\t\\')  # 整个字符串原样输出
    print('''line1
    line2
    line3''')  # 换行输出

    #  多行字符串'''...'''还可以在前面加上r使用，请自行测试：
    print(r'''line1
    hello \\\\''')  # 换行且原样输出

    print(ord('A'))  # 字符串转换
    print(chr(66))
    print('A'.encode('ascii'))  # 当str和bytes互相转换时，需要指定编码。最常用的编码是UTF-8
    print(b'A'.decode('ascii'))

    print('hello %s' % 'world')  # 格式化输出 %
    print('hello {0}, {1:.1f}'.format('world', 3.14))  # 格式化输出 format
    r = 2.5
    s = 3.14 * r ** 2
    print(f'The area of a circle with radius {r} is {s:.2f}')  # 格式化输出 f-string
    # 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
    s1 = 72
    s2 = 85
    r = (s2 - s1) / s2 * 100
    print(f'小明成绩提升的百分点为{r:.1f}')

    print(True, False)  # bool类型
    print(True and False)
    print(True or False)
    print(not True)

    # 空值
    print(None)  # 空值

    PI = 3.14  # 常量，全部大写为常量，定义上不可修改，实际可以修改，还是一个变量
    print(PI)

    x = 11
    y = 3
    print(x * y)  # 乘法
    print(x / y)  # 除法，结果为浮点数
    print(x // y)  # 整除
    print(x % y)  # 取模

    # list
    classmates = ['Michael', 'Bob', 'Tracy']  # list
    print(classmates)
    print(len(classmates))
    print(classmates[0])  # 索引越界：IndexError: list index out of range
    print(classmates[-1])
    classmates.append('Tom')
    print(classmates)
    classmates.pop()  # 尾部开始删除
    print(classmates)
    classmates.pop(1)  # 指定位置删除
    print(classmates)
    # 请用索引取出下面list的指定元素：
    L = [
        ['Apple', 'Google', 'Microsoft'],
        ['Java', 'Python', 'Ruby', 'PHP'],
        ['Adam', 'Bart', 'Lisa']
    ]
    # 打印Apple:
    print(L[0][0])
    # 打印Python:
    print(L[1][1])
    # 打印Lisa:
    print(L[2][2])

    # 元组
    classmates = ('Michael', 'Bob', 'Tracy')  # 元组，初始化后不能修改
    print(classmates)
    print(())  # 空元组
    print((1,))  # 定义一个元素的元组

    # dict特点：
    # 查找和插入的速度极快，不会随着key的增加而变慢；
    # 需要占用大量的内存，内存浪费多。
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}  # dict字典
    print(d)
    print(d['Bob'])
    # print(d['Tom']) # KeyError: 'Tom'
    print('Tom' in d)
    print(d.get('Tom'))  # key不存在返回None
    print(d.get('Tom'), 'Tom')  # 如果key不存在，返回指定值，如果key存在同样也会返回指定值
    d.pop('Bob')
    # d.pop('Bob')  # 删除不存在key报错，KeyError: 'Bob'
    print(d)

    # set类型 key不能重复
    s = set([1, 2, 3])
    print(s)
    s.add(4)
    print(s)
    s.add(4)
    print(s)
    s.remove(4)
    print(s)
    s1 = set([1, 2, 3])
    s2 = set([2, 3, 4])
    print(s1 & s2)  # 交集
    print(s1 | s2)  # 并集
