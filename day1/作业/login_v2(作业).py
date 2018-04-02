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
max_count = 3
temp_user = []

while count <= max_count:
    login_status = False
    sign_out_status = False
    print("#" * 55)
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "" or password == "":
        print("\033[0;31;0m用户名或密码不能为空！\033[0m")
        continue
    for i in info:
        if username == i["username"] and password == i["password"]:
            print("登录成功！欢迎\033[0;31;0m<%s>\033[0m" % (username,))
            login_status = True
            count = 0
            temp_user.clear()
            break
    if login_status == False:
        print("\033[0;31;0m登录失败！用户名或者密码错误！\033[0m")
        count = 0
        temp_user.append(username)
        if temp_user.count(username) >= 3:
            while True:
                choice = input("用户\033[0;31;0m<%s>\033[0m输入错误超过3次，是否继续？" % (username,))
                if choice == "y" or choice == "Y":
                    count = 0
                    temp_user.clear()
                    break
                elif choice == "n" or choice == "N":
                    sign_out_status = True
                    break
                else:
                    print("请输入\033[0;31;0mY/N\033[0;31;0m。")
    if sign_out_status == True:
        print("Bye!!!")
        break
    count += 1
