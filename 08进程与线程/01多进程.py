# coding:utf-8
import json
import multiprocessing
import os
import time


def work_a(lock):
    lock.acquire()
    for i in range(10):
        print(i, 'a', os.getpid())
        time.sleep(1)
    lock.release()


def work_b():
    for i in range(10):
        print(i, 'b', os.getpid())
        time.sleep(1)


class work(object):
    def __init__(self, q):
        self.q = q

    def send(self, msg):
        if not isinstance(msg, str):
            msg = json.dumps(msg)
        self.q.put(msg)

    def recv(self):
        while True:
            result = self.q.get()
            try:
                res = json.loads(result)
            except:
                res = result
            print('recv is %s' % res)



if __name__ == '__main__':
    # proc1 = multiprocessing.Process(target=work_a)
    # proc1.start()
    # proc1 = multiprocessing.Process(target=work_b)
    # proc1.start()

    # 进程池
    # pool = multiprocessing.Pool(5)
    # manger = multiprocessing.Manager()
    # lock = manger.Lock()
    # for i in range(20):
    #     pool.apply_async(func=work_a, args=(lock,))
    # pool.close()
    # pool.join()

    # 队列
    q = multiprocessing.Queue()
    w = work(q)
    send = multiprocessing.Process(target=w.send, args=({'name': 1},))
    recv = multiprocessing.Process(target=w.recv)

    send.start()
    recv.start()
    send.join()
    recv.terminate()

