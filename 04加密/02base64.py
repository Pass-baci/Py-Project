# coding=utf-8
import base64


def encode(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    elif isinstance(data, bytes):
        data = data
    else:
        raise TypeError('data need bytes or str')
    return base64.encodebytes(data).decode('utf-8')


def decode(data):
    if not isinstance(data, bytes):
        raise TypeError('data need bytes')
    return base64.decodebytes(data).decode('utf-8')


if __name__ == '__main__':
    res = encode('abc')
    print(res)
    print(decode(res.encode('utf-8')))
