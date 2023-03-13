# coding=utf-8
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s []line:%(lineno)s %(levelname)s %(message)s', filename='log.log', filemode='a')
    logging.info('hello')
