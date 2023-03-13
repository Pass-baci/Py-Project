# coding:utf-8
import multiprocessing
import os
import queue
import random
import threading
import time


def work_process(q):
    # for i in range(10):
    #     print('%s_%s_process', i, os.getpid())
    print('process_%s' % os.getpid())
    q.put('msg')
    q1 = queue.Queue()
    q1.put(q.get())
    t = threading.Thread(target=work_thread, args=(q1,))
    t.start()
    t.join()


lists = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

new_lists = []


def work_thread(q):
    print('thread_%s' % os.getpid())
    print('thread_msg_%s' % q.get())
    for i in range(5):
        print(i)
        time.sleep(1)


if __name__ == '__main__':
    q = multiprocessing.Queue()
    print('main_%s' % os.getpid())
    proc = multiprocessing.Process(target=work_process, args=(q,))
    proc.start()
    proc.join()
