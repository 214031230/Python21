#!/usr/bin/env python3
from core import login
from core import public
import pymysql


def choice():
    """
    功能选择，登录或者注册
    :return:
    """
    print("""
        请选择功能：1、登录 2、注册
    """)
    while 1:
        ch = input("请选择功能(输入功能ID)：").strip()
        if not ch:continue
        if ch == "1":
            start_login()
            break
        elif ch == "2":
            try:
                start_register()
            except pymysql.err.IntegrityError:
                print("Error:用户已存在")
            break
        else:
            print("Error：请输入正确的ID")


def start_login():
    """
    用户登录
    :return:
    """
    log = public.Public.log()
    count = 0
    while count < 3:
        user = input("user:").strip()
        password = input("password:").strip()
        if not user or not password:
            print("Error:用户名密码不能为空！")
            continue
        loginobj = login.Login(user, password)
        if loginobj.login():
            print("INFO:登录成功！")
            log.info("登录成功")
            break
        else:
            print("Error:用户名或密码错误")
            log.error("用户名或密码错误")


def start_register():
    """
    用户注册
    :return:
    """
    log = public.Public.log()
    count = 0
    while count < 3:
        user = input("user:").strip()
        password = input("password:").strip()
        if not user or not password:
            print("Error:用户名密码不能为空！")
            continue
        loginobj = login.Login(user, password)
        if loginobj.register():
            print("INFO:注册成功！")
            log.info("注册成功")
            break
        else:
            print("Error:注册失败！")
            log.error("注册失败")
