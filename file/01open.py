# coding=utf-8

import os


def write_file(path, message):
    f = os.open(path, os.O_CREAT|os.O_WRONLY|os.O_APPEND)
    try:
        if not message.endswith('\n'):
            message += '\n'
        os.write(f, message.encode('utf-8'))
    except Exception as e:
        print(e)
    finally:
        os.close(f)

def read_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError
    f = os.open(path, os.O_RDONLY)
    state = True
    content = b''
    while state:
        b = os.read(f, 100)
        if len(b) == 0:
            state = False
        else:
            content += b
    os.close(f)
    print(content.decode('utf-8'))

if __name__ == '__main__':
    curr_path = os.getcwd()
    path = os.path.join(curr_path, 'test1')
    write_file(path, 'abc 你好')
    read_file(path)
