#!/usr/bin/env python3
"""
购物车需求：
1、用户登录以后才可以购买商品
2、用户登录失败3次则被锁定
3、用户第一次登录需要充值金额，第二次登录显示可用余额
4、打印商品列表，让用户根据序号选择商品，加入购物车
5、购买商品，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
6、用户退出以后打印购物车
7、用户登录可以查购物历史
注释： 用户信息存在user_file文件里面
       被锁定用户存在user_lock_file文件里面
       用户余额存在user_
"""
goods = [{"name": "电脑", "price": 1999},
         {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998}]

login_mac_count = 3
count = 0
while count < login_mac_count:
    print("".center(20,"-"))
    print("\033[0;31;0m<欢迎访问SPF商城>\033[0m")
    print("".center(20, "-"))


