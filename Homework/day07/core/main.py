#!/usr/bin/env python3
from sys import modules
from core.manager import Manager
from core.my_pickle import MyPickle
from conf import config

def login():
    print("\033[0;31;0m")
    print("欢迎访问校园管理系统".center(50, "-"))
    print(">>>请登录：\033[0m")
    count = 0
    while count < 3:
        username = input("\033[0;35;0m>>>请输入用户名：\033[0m").strip()
        password = input("\033[0;35;0m>>>请输入密码：\033[0m").strip()
        if not username or not password:
            print("ERROR:用户名或密码不能为空")
        ret = MyPickle(config.userinfo)
        user_info = ret.load()
        print(user_info)
        if username in user_info["name"]:
            pwd_index = user_info["name"].index(username)
            if password == user_info["password"][pwd_index]:
                return username, user_info["type"][pwd_index]
            else:
                print("ERROR：密码错误")
        else:
            print("ERROR：用户名不存在")
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
            for i in obj.menus:
                print("\033[1;36;0m%s\033[0m" % i[0])
            choice = input("\033[0;35;0m>>>请选择功能：\033[0m").strip()
            try:
                func = obj.menus[int(choice) - 1][1]
                getattr(obj, func)()
            except ValueError:
                print("ERROR：请输入正确的ID")
            except IndexError:
                print("ERROR：请输入正确的ID")

