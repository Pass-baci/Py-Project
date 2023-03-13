# coding=utf-8

from db.mysql_db import pool


class UserDao:
    def login(self, username, password):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT COUNT(*) FROM t_user WHERE username=%s AND " \
                  "AES_DECRYPT(UNHEX(password),'HelloWorld')=%s"
            cursor.execute(sql, (username, password))
            count = cursor.fetchone()[0]
            return True if count == 1 else False
        except Exception as e:
            raise e
        finally:
            if "con" in dir():
                con.close()

    def get_user_role(self, username):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT r.role FROM t_user u JOIN t_role r ON u.role_id = r.id WHERE username=%s"
            cursor.execute(sql, (username,))
            role = cursor.fetchone()[0]
            return role
        except Exception as e:
            raise e
        finally:
            if "con" in dir():
                con.close()
