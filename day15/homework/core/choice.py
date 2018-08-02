#!/usr/bin/env python3
from core import login
from core import public
import pymysql


class Choice:
    @staticmethod
    def choice():
        """
        功能选择，登录或者注册
        :return:
        """
        print("""
            请选择功能：1、登录 2、注册
            测试账号：spf 密码：123
        """)
        view = {"1": "login", "2": "register"}
        while 1:
            ch = input("请选择功能(输入功能ID)：").strip()
            if not ch: continue
            if ch in view:
                try:
                    Choice.start(view[ch])
                except pymysql.err.IntegrityError:
                    print("Error:用户名已经存在")
                except Exception as e:
                    print("Error: %s" % e)
            else:
                print("Error：请输入正确的ID")

    @staticmethod
    def start(obj):
        """
        用户登录/注册
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
            login_obj = login.Login(user, password)
            if getattr(login_obj, obj)():
                print("INFO: %s Success！" % obj)
                log.info("%s Success" % obj)
                break
            else:
                print("Error: %s fail" % obj)
                log.error("Error: %s fail" % obj)
