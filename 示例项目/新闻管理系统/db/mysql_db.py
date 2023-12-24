# coding=utf-8

import mysql.connector.pooling

__config = {
    "host": "192.168.230.135",
    "port": "3306",
    "user": "root",
    "password": "root",
    "database": "vega",
}

try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **__config,
        pool_size=10,
    )
except Exception as e:
    raise e
