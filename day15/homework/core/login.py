#!/usr/bin/env python3
from core import mysql
import hashlib


class Login:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def __md5(self):
        """
        md5加密（动态加盐）
        :return: 密码
        """
        md5obj = hashlib.md5(self.user.encode("utf-8"))
        md5obj.update(self.password.encode("utf-8"))
        return md5obj.hexdigest()

    def login(self):
        """
        数据库验证登录
        :return: 
        """
        mysql_obj = mysql.Mysql("select id from user where username=%s and password=%s",
                                (self.user, self.__md5()))
        if mysql_obj.select():
            return True
        else:
            return False

    def register(self):
        """
        数据库注册验证
        :return:
        """
        mysql_obj = mysql.Mysql("insert into user(username,password) values(%s,%s)",
                                (self.user, self.__md5()))
        return mysql_obj.insert()
