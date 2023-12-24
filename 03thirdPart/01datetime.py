# coding:utf-8
import datetime

if __name__ == '__main__':
    print(datetime.datetime.now())
    print(datetime.datetime.now()-datetime.timedelta(days=1))
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
