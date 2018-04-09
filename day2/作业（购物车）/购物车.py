#!/usr/bin/env python3
import os
"""
购物车需求：
1、用户登录以后才可以购买商品
2、用户登录失败3次则被锁定
3、用户第一次登录需要充值金额，第二次登录显示可用余额
4、打印商品列表，让用户根据序号选择商品，加入购物车
5、购买商品，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
6、用户退出以后打印购物车
7、用户登录可以查购物历史
注释：  用户信息存在user_file文件里面
       被锁定用户存在user_lock_file文件里面
       用户余额存在user_money
       用户购买历史存在user_buy_his
"""
goods = [{"name": "电脑", "price": 1999},
         {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998}]

count = 0
fail_user = []
shopping_car = {}
flag = True
while flag:
    flag_login = False
    flag_check_lock = False
    print("".center(30,"-"))
    print("\033[0;31;0m<欢迎访问SPF商城>\033[0m".rjust(30, " "))
    print("".center(30, "-"))

    # 输入用户名和密码
    username = input("请输入用户名：").strip()
    password = input("请输入密码：").strip()

    # 判断用户是否被锁定 start
    user_lock_file = open("./user_lock_file", mode="r")
    for i in user_lock_file.readlines():
        _username, = i.split()
        if _username == username:
            print("用户已经被锁定！请联系管理员解锁！")
            flag_check_lock = True
    user_lock_file.close()
    if flag_check_lock == True:
        continue
    # 判断用户是否被锁定 end

    # 打开user_file文件
    userfile = open("./user_file", mode="r")
    # 判断用户登录
    for i in userfile.readlines():
        _username,_password = i.split()
        if username == _username and password == _password:
            print("登录成功！欢迎\033[0;31;0m<%s>\033[0m!" % (username,))
            flag_login = True
            # 检查用户是否充值过金额,如果没有则充值金额
            if os.path.exists("%s_money" % (username,)) != True:
                # 充值金额
                money = int(input("请充值金额："))
                money_file = open("./%s_money" % (username,), mode="w")
                money_file.write(str(money))
                money_file.close()
            else:
                # 显示用户余额
                money_file = open("./%s_money" % (username,), mode="r")
                print("您的账户余额：%s$" % (money_file.read(),))
                money_file.close()
            # 开始购物
            # 打印商品列表
            print("商品列表".center(20, "-"))
            for j in goods:
                print("%d. %s %d$" % (goods.index(j), j["name"], j["price"]))
            buy = input("请输入你要购买的商品名ID：")
            if buy.isdigit():
                buy = int(buy)
                print(goods[buy])
    userfile.close()
    # 用户登录失败操作
    if flag_login == False:
        print("\033[0;31;0m登录失败！用户名或者密码错误！\033[0m")
        # 如果用户连续输入错误超过3次，则锁定用户
        fail_user.append(username)
        if fail_user.count(username) == 3:
            print("用户<%s>连续输入错误超过3次，用户将被锁定!" % (username,))
            user_lock_file = open("./user_lock_file", mode="a")
            user_lock_file.write(username+"\n")
            user_lock_file.close()
    count += 1
