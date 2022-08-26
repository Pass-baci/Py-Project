#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

if __name__ == '__main__':
    # \d可以匹配一个数字
    # \w可以匹配一个字母或数字
    # .可以匹配任意字符
    # *表示任意个字符（包括0个）
    # 用+表示至少一个字符
    # 用?表示0个或1个字符
    # \s可以匹配一个空格（也包括Tab等空白符） \s+表示至少有一个空格
    # 用{n}表示n个字符
    # 用{n,m}表示n-m个字符
    # ^表示行的开头
    # $表示行的结束
    print(re.match(r'\d{3}\-\d{3,8}$', '010-12345'))

    # 切分字符串
    s = 'a b  c'
    print(s.split(' '))
    print(re.split(r'\s+', s))
    s = 'a, b  c'
    print(re.split(r'[\s\,]+', s))
    s = 'a;, b  c'
    print(re.split(r'[\s\,\;]+', s))

    # 分组
    m = re.match(r'(\d{3})-(\d{3,8})$', '010-123456')
    print(m.group(0), m.group(1), m.group(2))
