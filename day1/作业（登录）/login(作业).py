#!/usr/bin/env python3
"""
功能描述：
1、用户登陆，三次机会重试。
2、可以支持多用户登录
3、用户输入了三次机会，都没成功，给它一个选择，让它在试试(必须是同一个用户输入3次错误)
如果用户选择继续则再给他三次机会；如果选择退出则退出程序并打印 print('臭不要脸.....')
4、使用列表+字典存用户名和密码
"""
# 用户信息
info = [
    {"username": "sunpengfei", "password": "123456"},
    {"username": "guangtou", "password": "123456"},
    {"username": "jinxing", "password": "123456"}
]
count = 1
# 临时存储用户登录次数
temp_user = []
while True:
    # 登录标志位
    login_status = False
    # 退出标志位
    sign_out_status = False
    print("#" * 55)
    username = input("请输入用户名：")
    password = input("请输入密码：")
    # 用户名或者密码不能为空
    if username == "" or password == "":
        print("\033[0;31;0m用户名或密码不能为空！\033[0m")
        continue
    # 判断用户名和密码是否正确
    for i in info:
        if username == i["username"] and password == i["password"]:
            print("登录成功！欢迎\033[0;31;0m<%s>\033[0m" % (username,))
            # 用户登录成功则清除之前登录失败的记录
            temp_user.clear()
            # 登录成功则修改标志位为True,则不会执行登录失败操作
            login_status = True
            break
    # 由于用户没登录成功，login_status还是为False
    if login_status == False:
        print("\033[0;31;0m用户名或者密码错误，请重试！\033[0m")
        # 登录失败则添加当前用户到列表
        temp_user.append(username)
        # 如果用户登录失败次数大于等于3次
        if temp_user.count(username) >= 3:
            # while 作用让用户停留在选择界面
            while True:
                choice = input("用户\033[0;31;0m<%s>\033[0m已经登录失败超过3次，是否继续尝试？\033[0;31;0mY继续/N退出\033[0m：" % (username,))
                if choice.upper() == "Y":
                    # 用户选择继续尝试，则清除失败记录
                    temp_user.clear()
                    break
                elif choice == "n" or choice == "N":
                    print("\033[0;31;0m臭不要脸.....Bye!!!\033[0m")
                    # 如果用户选择退出，则修改标志位状态，因为直接break无法退出循环
                    sign_out_status = True
                    break
                else:
                    print("\033[0;31;0m请输入正确的Y或N！\033[0m")
    # 退出整个循环
    if sign_out_status == True:
        break
    count += 1
