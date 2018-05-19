#!/usr/bin/env python3
from sys import modules
from core.manager import Manager
from core import my_pickle
from conf import config
from core.public import *


def login():
    print_log("欢迎访问校园管理系统".center(50, "-"), None)
    count = 0
    while count < 3:
        username = input(">>>请输入用户名：").strip()
        password = input(">>>请输入密码：").strip()
        if not username or not password:
            print_log("用户名或密码不能为空", "error")
        user_info = my_pickle.load(config.userinfo)
        if username in user_info["name"]:
            pwd_index = user_info["name"].index(username)
            if password == user_info["password"][pwd_index]:
                return username, user_info["type"][pwd_index]
            else:
                print_log("密码错误", "error")
        else:
            print_log("用户名不存在", "error")
        count += 1


def main():
    """
    选择视图
    通过对象角色去调用对应的方法，根据用户选择跳转到对应的方法中
    :return:
    """
    ret = login()
    while True:
        if ret:
            role_class = getattr(modules[__name__], ret[1])
            obj = role_class(ret[0])
            print_log("-" * 60, None)
            for i in obj.menus:
                print_log("%s" % i[0], "menus")
            print_log("-" * 60, None)
            choice = input("\033[0;34;0m>>>请选择功能：\033[0m").strip()
            try:
                func = obj.menus[int(choice) - 1][1]
                getattr(obj, func)()
            except ValueError:
                print_log("请输入正确的ID", "error")
            except IndexError:
                print_log("请输入正确的ID", "error")

