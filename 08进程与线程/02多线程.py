# coding:utf-8
import concurrent.futures
import random
import threading
import time

lists = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

new_lists = []


def work():
    if len(lists) == 0:
        return
    data = random.choice(lists)
    lists.remove(data)
    new_data = '%s_new' % data
    new_lists.append(new_data)
    time.sleep(1)


def poll_work(i):
    print(i)
    time.sleep(1)


if __name__ == '__main__':
    # start = time.time()
    # t_list = []
    # for i in range(len(lists)):
    #     # work()
    #     t = threading.Thread(target=work)
    #     t_list.append(t)
    #     t.start()
    # for t in t_list:
    #     t.join()
    # print('old_lists: %s' % lists)
    # print('new_lists: %s' % new_lists)
    # print('time: %s' % (time.time()-start))

    # 线程池
    t_pool = concurrent.futures.ThreadPoolExecutor(3)
    for i in range(20):
        t_pool.submit(poll_work, (i,))
