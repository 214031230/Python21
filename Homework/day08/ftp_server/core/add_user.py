#!/usr/bin/env python3
from core.UserManager import User
from conf import settings
while True:
    user = input("请输入用户名：")
    pwd = input("请输入密码：")
    try:
        datasize = int(input("请输入磁盘配额："))
    except Exception as e:
        print("你输入的磁盘配额不是数字")
        continue
    user_obj = User(user, pwd)
    user_obj.add()
    user_obj.add_user_size(datasize)
    print("""
        创建用户成功:
            用户名： %s
            家目录   %s/%s
            磁盘配额：%s M
    """ % (user, settings.home_dir, user, datasize))
