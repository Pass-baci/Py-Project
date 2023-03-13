# coding=utf-8
import datetime
import hashlib

if __name__ == '__main__':
    h = hashlib.md5(b'abc')
    res = h.hexdigest()
    print(res)

    base_sign = 'token'
    token = '%s%s'.format(base_sign, datetime.datetime.now())
    hash_obj = hashlib.sha1(token.encode('utf-8'))
    print(hash_obj.hexdigest())

    hash_obj = hashlib.sha1(token.encode('utf-8'))
    print(hash_obj.hexdigest())
