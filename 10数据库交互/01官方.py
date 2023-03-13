# coding=utf-8

import mysql.connector

if __name__ == '__main__':
    con = mysql.connector.connect(
        host="192.168.230.135", port="3306",
        user="root", password="root",
        database="fcc_conf"
    )
    cursor = con.cursor()
    sql = "SELECT * FROM t_bank_account WHERE Fid=%s"
    cursor.execute(sql, ("100 OR 1=1",))
    for one in cursor:
        for field in one:
            print(field)
    # print(cursor.fetchone()[0])
    con.close()
