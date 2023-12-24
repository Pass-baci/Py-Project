# coding=utf-8
import sys
import time

from colorama import Fore, Style
from getpass import getpass
from service.user_service import UserService
import os

if __name__ == '__main__':
    __user_service = UserService()
    while True:
        os.system("cls")
        print(Fore.LIGHTBLUE_EX, "\n\t=====================")
        print(Fore.LIGHTWHITE_EX, "\n\tWelcome To News System")
        print(Fore.LIGHTBLUE_EX, "\n\t=====================")
        print(Fore.LIGHTWHITE_EX, "\n\t1. Login")
        print(Fore.LIGHTWHITE_EX, "\n\t2. Exit")
        print(Style.RESET_ALL)
        opt = input("\n\tPlease Input Number: ")

        if opt == "1":
            username = input("\n\tusername: ")
            password = getpass("\n\tpassword: ")
            state = __user_service.login(username, password)
            if state == True:
                role = __user_service.get_user_role(username)
                if role == "新闻编辑":
                    print("test")
                elif role == "管理员":
                    os.system("cls")
                    print(Fore.LIGHTWHITE_EX, "\n\t1. News Manage")
                    print(Fore.LIGHTWHITE_EX, "\n\t2. User Manage")
                    print(Fore.LIGHTWHITE_EX, "\n\t3. Exit User")
                    print(Fore.LIGHTWHITE_EX, "\n\t4. Exit System")
                    print(Style.RESET_ALL)
                    opt = input("\n\tPlease Input Number: ")
                    if opt == "1":
                        break
                    elif opt == "2":
                        break
                    elif opt == "3":
                        break
                    elif opt == "4":
                        sys.exit(0)
            else:
                print(Fore.LIGHTWHITE_EX, "\n\tusername or password failed")
                time.sleep(2)
        elif opt == "2":
            sys.exit(0)
