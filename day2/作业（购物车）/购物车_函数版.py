#!/usr/bin/env python3
import os
import time

# day2 博客地址：http://www.cnblogs.com/spf21/p/8734989.html

"""
购物车需求：
1、用户登录以后才可以购买商品
2、用户登录失败3次则被锁定
3、用户第一次登录需要充值金额，第二次登录显示可用余额
4、打印商品列表，让用户根据序号选择商品，加入购物车
5、购买商品，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
6、用户退出以后打印购物车
7、用户登录可以查购物历史
8、用户约不足的时候可以充值余额
注释：  用户信息存在user_file文件里面  测试用户：wxx 密码：123
       被锁定用户存在user_lock_file文件里面
       用户余额存在%user_money
       用户购买历史存在%user_his
"""
goods = [{"name": "电脑", "price": 1999},
         {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998}]

fail_user = []
flag = True
print("".center(35, "="))
print("\033[0;34;0m<欢迎访问SPF商城>\033[0m".rjust(32, " "))
print("".center(35, "="))
print("\033[0;31;0m<请先登录，登录后才可以购买商品!>\033[0m")
while flag:
    flag_login = False
    flag_check_lock = False
    # 输入用户名和密码
    username = input(">>>请输入用户名：").strip()
    password = input(">>>请输入密码：").strip()

    # 判断用户名或密码不能为空
    if username == "" or password == "":
        print("\033[0;31;0m用户名或者密码不能为空\033[0m")
        continue
    # 判断用户是否被锁定
    user_lock_file = open("./file/user_lock_file", mode="r")
    for i in user_lock_file.readlines():
        _username, = i.split()
        if _username == username:
            print("\033[0;31;0m用户已经被锁定！请联系管理员解锁！\033[0m")
            flag_check_lock = True
    user_lock_file.close()

    # 用户已经被锁定，则返回登录界面
    if flag_check_lock == True:continue

    # 判断用户登录
    user_file = open("./file/user_file", mode="r")
    for i in user_file.readlines():
        _username, _password = i.split()
        if username == _username and password == _password:
            print("-"*25)
            print("")
            print("\033[0;33;0m登录成功！欢迎：\033[0;33;0m<%s>\033[0m\033[0m" % (username,))
            flag_login = True

            # 检查用户是否充值过金额,如果没有则充值金额
            # 充值金额
            if os.path.exists("./file/%s_money" % (username,)) != True:
                while True:
                    money = input(">>>请充值金额：").strip()
                    if money.isdigit():
                        money = int(money)
                        money_file = open("./file/%s_money" % (username,), mode="w")
                        money_file.write(str(money))
                        money_file.close()
                        break
                    else:
                        print("\033[0;31;0m请输入正确的金额！\033[0m")
                        continue
            # 显示用户余额
            else:
                money_file = open("./file/%s_money" % (username,), mode="r")
                for x in money_file.readlines():
                    money, = x.split()
                money_file.close()
                print("-" * 24)
                print("")
                print("\033[0;35;0m你的账户余额：%s $\033[0m" % (money,))
                money = int(money)
            # 开始购物，打印商品列表
            while flag:
                print("\033[0;33;0m商品列表\033[0m".center(35, "-"))
                print("")
                print("\033[0;31;0m商品ID   商品名称    商品价格\033[0m")
                for j in goods:
                    print("\033[0;33;0m%d        %s       %d$\033[0m" % (goods.index(j), j["name"], j["price"]))
                print("")
                print("-" * 25)
                buy = input(">>>请输入你要购买的商品名ID(\033[0;31;0mq退出/h查看购物车/s查看余额\033[0m)：").strip()
                # 购买商品
                if buy.isdigit():
                    buy = int(buy)
                    # 判断用户输入的商品编号是否存在
                    if buy > (len(goods) - 1):
                        print("\033[0;31;0m你输入的商品ID不存在！\033[0m")
                        continue
                    # 选择购买数量
                    choice_number = input(">>>请选择购买的数量：")
                    if choice_number.isdigit():
                        choice_number = int(choice_number)
                        # 判断余额是否充足
                        if (goods[buy]["price"] * int(choice_number)) < money:
                            print("-"*25)
                            print("\033[0;36;0m你已经成功添加%s个<%s>到购物车！\033[0m" % (choice_number, goods[buy]["name"]))
                            # 保存购物车
                            count = 1
                            while count <= int(choice_number):
                                date = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
                                user_his = open("./file/%s_his" % (username,), mode="a")
                                user_his.write("%s  %s\n" % (goods[buy]["name"], date))
                                user_his.close()
                                count += 1
                            # 保存余额
                            money = money - (goods[buy]["price"] * int(choice_number))
                            money_file = open("./file/%s_money" % (username,), mode="w")
                            money_file.write(str(money))
                            money_file.close()
                        else:
                            choice = input("\033[0;31;0m>>>余额不足！是否进行充值Y/N：\033[0m").strip()
                            # 充值
                            if choice == "y" or choice == "Y":
                                recharge = input(">>>请充值金额：").strip()
                                if recharge.isdigit():
                                    recharge = int(recharge)
                                    money_file = open("./file/%s_money" % (username,), mode="w")
                                    money_file.write(str(money + recharge))
                                    money_file.close()
                                    money = money + recharge
                                    continue
                                else:
                                    print("\033[0;31;0m请输入正确的金额！\033[0m")
                                    continue
                            elif choice == "N" or choice == "n":
                                continue
                            else:
                                print("-"*25)
                                print("\033[0;31;0m请输入正确的指令！\033[0m")
                    else:
                        print("\033[0;31;0m请输入正确的数量！\033[0m")
                elif buy == "Q" or buy == "q":
                    print("\033[0;33;0m Bye Bye!!!\033[0m")
                    flag = False

                # 查看购物车
                elif buy == "h" or buy == "H":
                    if os.path.exists("./file/%s_his" % (username,)) == True:
                        buy_his = open("./file/%s_his" % (username,), mode="r")
                        print("-" * 35)
                        print("\033[0;33;0m购物车：\033[0m")
                        count_i = 1
                        for his in buy_his.readlines():
                            # print(his.split(),type(his.split()))
                            shop, d = his.split()
                            print("\033[0;33;0m%s.%s 购买时间：%s\033[0m" % (count_i, shop, d))
                            count_i += 1
                    else:
                        print("\033[0;33;0m你还未购买任何商品！\033[0m")
                # 查看账户余额
                elif buy == "s" or buy == "S":
                    money_file = open("./file/%s_money" % (username,), mode="r")
                    for x in money_file.readlines():
                        money, = x.split()
                    money_file.close()
                    money = int(money)
                    print("-" * 24)
                    print("\033[0;35;0m你的账户余额：%s$\033[0m" % (money,))
                else:
                    print("-"*25)
                    print("\033[0;31;0m请输入正确指令！\033[0m")
    user_file.close()
    # 用户登录失败操作
    if flag_login == False:
        print("\033[0;31;0m登录失败！用户名或者密码错误!\033[0m")
        # 如果用户连续输入错误超过3次，则锁定用户
        fail_user.append(username)
        if fail_user.count(username) == 3:
            print("\033[0;31;0m用户<%s>连续输入错误超过3次，用户将被锁定!\033[0m" % (username,))
            user_lock_file = open("./file/user_lock_file", mode="a")
            user_lock_file.write(username+"\n")
            user_lock_file.close()