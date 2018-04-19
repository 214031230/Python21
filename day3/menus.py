#!/usr/bin/env python3


def check_login(argv):
    """检测用户状态
    return 0 用户未登录
    return 2 用户从未登录过
    """
    def inner(username):
        with open("./file/user_pid") as f1:
            for i in f1:
                if username in i:
                    user, pid = i.split()
                    if pid == 0:
                        return 0
                    else:
                        argv(username)
                else:
                    return 2
    return inner


def update_login_status(argv):
    """修改用户登录状态"""
    def inner(*args):
        res = argv(*args)
        if res == 0:
            import os
            with open("./file/user_pid") as f1, open("./file/user_pid.bak", mode="a") as f2:
                for i in f1:
                    user, pid = i.split()
                    pid = int(pid)
                    if username in i:
                        f2.write("%s %s\n" % (username, 1))
                        continue
                    else:
                        f2.write("%s %s\n" % (user, pid))
            os.remove("./file/user_pid")
            os.rename("./file/user_pid.bak", "./file/user_pid")
        elif res == 1:
            import os
            with open("./file/user_pid") as f1, open("./file/user_pid.bak", mode="a") as f2:
                for i in f1:
                    user, pid = i.split()
                    pid = int(pid)
                    if username in i:
                        f2.write("%s %s\n" % (username, 0))
                        continue
                    else:
                        f2.write("%s %s\n" % (user, pid))
            os.remove("./file/user_pid")
            os.rename("./file/user_pid.bak", "./file/user_pid")
        elif res == 2:
            with open("./file/user_pid", mode="a") as f1:
                f1.write("%s %s\n" % (username, 1))
    return inner


@update_login_status
def login(username, password):
    """登录"""
    if not username or not password:
        print("用户名或密码不能为空")
    with open("./file/user_list") as f1:
        for i in f1:
            user, passwd = i.split()
            if username == user and password == passwd:
                print("登录成功！")
                return 0
        else:
            print("用户名或者密码错误，请重试！")


@update_login_status
def registered(username, password):
    """注册"""
    if not username or not password:
        print("用户名或者密码不能为空！")

    with open("./file/user_list", mode="r") as f1, open("./file/user_list", mode="a") as f2:
        for i in f1:
            if username in i:
                print("用户名已经存在！请重新注册")
                break
        else:
            f2.write("%s %s\n" % (username, password))
            print("注册成功！")
            return 2


@check_login
def article_page(username):
    """文章页面"""
    print("文章页面")


@check_login
def logs_page(username):
    """日记页面"""
    pass


@check_login
def comment_page(username):
    """评论页面"""
    pass


@check_login
def collection_page(username):
    """收藏页面"""
    pass


@update_login_status
def log_out(username):
    """注销"""
    return 1


def blog_exit():
    exit()
    """退出"""

# username = input("请输入用户名：").strip()
# password = input("请输入密码：").strip()
# username = "allen"
# password = "123"
# login(username, password)
# registered(username, password)
# log_out("wxx")
