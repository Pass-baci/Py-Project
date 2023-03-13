# coding=utf-8

from db.user_dao import UserDao


class UserService:
    __user__dao = UserDao()

    def login(self, username, password):
        try:
            res = self.__user__dao.login(username, password)
            return res
        except Exception as e:
            print(e)

    def get_user_role(self, username):
        try:
            res = self.__user__dao.get_user_role(username)
            return res
        except Exception as e:
            print(e)
