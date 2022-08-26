#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone
from collections import namedtuple, deque, defaultdict, OrderedDict

if __name__ == '__main__':
    print(datetime.now())
    print(datetime(2022, 4, 19, 12, 20))
    print(datetime(2022, 4, 19, 12, 20).timestamp())  # 时间戳
    t = datetime.now().timestamp()
    print(datetime.fromtimestamp(t))
    print(datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S'))
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(datetime.now() + timedelta(hours=1))
    print(datetime.now() - timedelta(days=1))
    print(datetime.now().replace(tzinfo=timezone(timedelta(hours=8))))

    # 创建元组的类
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p.x, p.y)
    print(isinstance(p, tuple))
    # 创建队列
    q = deque(['A', 'B', 'C'])
    q.append('D')
    q.appendleft('X')
    print(q.pop())
    print((q.popleft()))
    # key不存在返回自己定义的默认值的Dict
    dd = defaultdict(lambda: 'N/A')
    dd['key1'] = 'ABC'
    print(dd['key1'])
    print(dd['key2'])
    # 保证dict遍历是有序的
    d = dict([('a', 1), ('b', 2), ('c', 3)])
    print(d)
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print(od)
