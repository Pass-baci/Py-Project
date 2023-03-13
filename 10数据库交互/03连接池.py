# coding=utf-8

import mysql.connector.pooling

if __name__ == '__main__':
    pool = mysql.connector.pooling.MySQLConnectionPool(
        host="192.168.230.135", port="3306",
        user="root", password="root",
        database="fcc_conf", pool_size=10
    )
    con = pool.get_connection()
    cursor = con.cursor()
    sql = "SELECT * FROM t_bank_account WHERE Fid=%s"
    cursor.execute(sql, ("100",))
