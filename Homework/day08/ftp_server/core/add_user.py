#!/usr/bin/env python3
from core.UserManager import User
user = input("用户名：")
pwd = input("密码：")
user_obj = User(user, pwd)
user_obj.add()