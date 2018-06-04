#!/usr/bin/env python3
import hashlib
import os
from conf import settings
from core.MyJson import MyJson
from core.Pubulic import Public


class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.__home_size = settings.home_size
        self.user_info = settings.user_info
        self.user_size = settings.user_size
        self.user_dic = MyJson.load(self.user_info)
        self.user_size_dic = MyJson.load(self.user_size)
        self.log = Public.log()

    def __encrypt(self):
        """密码进行MD5加密,动态加盐方式"""
        md5obj = hashlib.md5(self.username.encode("utf-8"))
        md5obj.update(self.__password.encode("utf-8"))
        return md5obj.hexdigest()

    def add(self):
        """增加用户，用户创建成功返回True 失败（用户已经存在）返回False"""
        if self.user_dic.get(self.username):
            return False
        else:
            password = self.__encrypt()
            self.user_dic[self.username] = password
            MyJson.dump(self.user_dic, self.user_info)
            home_path = os.path.join(settings.home_dir, self.username)
            if not os.path.exists(home_path):
                os.mkdir(home_path)
            self.log.info("创建%s用户成功" % self.username)
            self.add_user_size()
            print("%s创建成功" % self.username)
            return True

    def add_user_size(self):
        """配置用户的磁盘配额"""
        self.user_size_dic[self.username] = self.__home_size
        MyJson.dump(self.user_size_dic, self.user_size)
        self.log.info("%s用户的磁盘配额为%s" % (self.username, self.__home_size))

    def login(self):
        """用户登录，登录成功返回True 失败返回False"""
        for i in self.user_dic:
            password = self.__encrypt()
            if self.username == i and password == self.user_dic[i]:
                print("%s登录成功" % self.username)
                return True
        else:
            return False
