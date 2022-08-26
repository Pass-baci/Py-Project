#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import multiprocessing
import os
import threading
import time


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        # time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


balance = 0
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()


def loop1():
    x = 0
    while True:
        x = x ^ 1


local_school = threading.local()


def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()


def main():
    # 多进程
    # print('Process (%s) start...' % os.getpid())
    # pid = os.fork()
    # if pid == 0:
    #     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    # else:
    #     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

    # 多线程
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)

    # 多核处理
    print(multiprocessing.cpu_count())
    for i in range(multiprocessing.cpu_count()):
        t = threading.Thread(target=loop1)
        t.start()

    # threadLocal[解决一个线程间各个函数的传参问题]
    t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()


main()
