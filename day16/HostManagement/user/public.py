#!/usr/bin/env python3
import hashlib


class Public:
    @staticmethod
    def md5(user, pwd):
        """
        md5加密（采用动态加盐加密）
        :param user: 用户名
        :param pwd: 密码
        :return: 加密后的密码
        """
        obj = hashlib.md5(user.encode("utf-8"))
        obj.update(pwd.encode("utf-8"))
        return obj.hexdigest()



