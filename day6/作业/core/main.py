#!/usr/bin/env python3
import sys
from conf import config
import json
from core import manager

def tab_dump(dic, t_name):
    """
    把字典序列化到内存中
    :param dic: 字典，存储表数据
    :param t_name:  表名称
    :return:
    """
    f = open(t_name, mode="w")
    json.dump(dic, f)
    f.close()


def tab_load(t_name):
    """
    把表内容反序列化成字典
    :param t_name: 表名称
    :return: 返回一个字典
    """
    f = open(t_name)
    dic = json.load(f)
    f.close()
    return dic


def login():
    """
    用户登录
    :return: 登录成功返回用户名和身份teacher  student admin
    """
    print(">>欢迎登录：")
    count = 0
    while count < 3:
        username = input("\033[0;35;0m请输入用户名：\033[0m").strip()
        password = input("\033[0;35;0m请输入密码：\033[0m").strip()
        if not username or not password:
            print("ERROR:用户名或密码不能为空")
        user_info = tab_load(config.userinfo)
        if username in user_info["username"]:
            pwd_index = user_info["username"].index(username)
            if password == user_info["password"][pwd_index]:
                return username, user_info["usertype"][pwd_index]
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
    if ret:
        print(ret)
        role_class = getattr(sys.modules[__name__], ret[1])
        obj = role_class(ret[0])
        print(obj)
        # for i in obj.menus:
        #     print(i)