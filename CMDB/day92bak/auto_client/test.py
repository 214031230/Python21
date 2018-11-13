#!/usr/bin/env python3
import requests
import hashlib
import time


def md5(arg):
    """
    MD5加密
    :param arg:
    :return:
    """
    hs = hashlib.md5()
    hs.update(arg.encode("utf-8"))
    return hs.hexdigest()


def run():
    # 取到当前时间
    c_time = str(time.time())
    # 当前时间和key结合生成动态key
    new_key = "%s|%s" % ("324SD2342SD242FSFS2", c_time)
    # 对动态key进行加密
    ret = md5(new_key)
    # 生成头信息
    auth_header_val = "%s|%s" % (ret, c_time)
    # 发送key信息进行验证
    response = requests.get("http://127.0.0.1:8000/api/test.html", headers={"auth-api": auth_header_val})
    print(response.text)


run()
