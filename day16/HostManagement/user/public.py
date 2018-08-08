#!/usr/bin/env python3
import hashlib
import random


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

    @staticmethod
    def code(n):
        """
        随机验证码
        :param n: 验证码长度
        :return: 返回验证码
        """
        code = ""
        for i in range(n):
            big_letter = chr(random.randint(65, 90))
            letter = chr(random.randint(97, 122))
            number = str(random.randint(0, 9))
            code += random.choice([big_letter, letter, number])
        return code