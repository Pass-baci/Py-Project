# coding=utf-8

import mysql.connector

if __name__ == '__main__':
    try:
        con = mysql.connector.connect(
            host="192.168.230.135", port="3306",
            user="root", password="root",
            database="test"
        )
        con.start_transaction()
        cursor = con.cursor()
        sql = "INSERT INTO `character` (`str`) VALUES ('test')"
        sql2 = "INSERT INTO `character` (`str1`) VALUES ('test1')"
        cursor.execute(sql)
        cursor.execute(sql2)
        con.commit()
    except Exception as e:
        print(e)
        if "con" in dir():
            con.rollback()
    finally:
        if "con" in dir():
            con.close()
