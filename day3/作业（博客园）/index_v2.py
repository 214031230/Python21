#!/usr/bin/env python3
# day3博客地址：http://www.cnblogs.com/spf21/p/8850060.html
"""作业需求
1)，启动程序，首页面应该显示成如下格式：
    欢迎来到博客园首页
    1:请登录
    2:请注册
    3:文章页面
    4:日记页面
    5:评论页面
    6:收藏页面
    7:注销
    8:退出程序
2)，用户输入选项，3~6选项必须在用户登录成功之后，才能访问成功。
3)，用户选择登录，用户名密码从register文件中读取验证，三次机会，没成功则结束整个程	序运行，成功之后，
可以选择访问3~6项.
4)，如果用户没有注册，则可以选择注册，注册成功之后，可以自动完成登录，然后进入首页选择。
5)，注销用户是指注销用户的登录状态，使其在访问任何页面时，必须重新登录。
6)，退出程序为结束整个程序运行。

测试账号：wxx  密码：123
测试账号：spf  密码：123
"""
import time


def run_log(func, user):
    """记录用户调用函数日志"""
    with open("./file/fun_run_log", mode="a", encoding="utf-8") as f1:
        timer = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        f1.write("时间：%s 用户：%s 运行函数：%s\n" % (timer, user, func))


def wrapper_outer(run_log_func):
    def wrapper(main_func):
        def inner(*args, **kwargs):
            if user_status["user"] and user_status["status"]:
                result = main_func(*args, **kwargs)
                if result != None:
                    return result
            else:
                str_func = "%s " % (main_func,)
                if "blog_exit" in str_func:
                    print("\033[0;31;0mBye Bye!!!\033[0m".center(40, "-"))
                    exit()
                if "log_out" in str_func:
                    print("\033[0;31;0m用户未登录!!!\033[0m")
                    exit()
                print("\n\033[0;35;0m>>>欢迎登录：\033[0m")
                count = 0
                while count < 3:
                    username = input("\033[0;35;0m请输入用户名：\033[0m").strip()
                    password = input("\033[0;35;0m请输入密码：\033[0m").strip()
                    if not username or not password:
                        print("\033[0;35;0m用户名或密码不能为空\033[0m")
                    with open("./file/user_list") as f1:
                        for i in f1:
                            user, passwd = i.split()
                            if username == user and password == passwd:
                                print("\n\033[0;35;0m登录成功！欢迎:<%s>\n\033[0m" % (username,))
                                user_status["user"] = username
                                user_status["status"] = True
                                return username
                        else:
                            print("\033[0;35;0m用户名或者密码错误，请重试！\033[0m")
                    count += 1
                else:
                    exit()
            res_run_log = run_log_func(main_func, user_status["user"])
            if res_run_log != None:
                return run_log_func
        return inner
    return wrapper


@wrapper_outer(run_log)
def login():
    if user_status["user"] and user_status["status"]:
        print("\033[0;31;0m%s用户已经登录！！！\033[0m" % (user_status["user"],))


def registered():
    """注册"""
    print("\033[0;35;0m\n>>>欢迎注册:")
    if user_status["user"] and user_status["status"]:
        print("\033[0;31;0m 当前用户：%s 请先注销在注册！\033[0m" % (user_status["user"],))
    else:
        flag = True
        while flag:
            username = input("\033[0;35;0m请输入用户名：").strip()
            first_password = input("\033[0;35;0m请输入密码：").strip()
            second_password = input("\033[0;35;0m请确认密码：").strip()

            if not username or not first_password or not second_password:
                print("\033[0;35;0m用户名或者密码不能为空！")
                continue

            if first_password != second_password:
                print("\033[0;35;0m两次密码输入不一致，请重新输入！")
                continue

            with open("./file/user_list", mode="r") as f1, open("./file/user_list", mode="a") as f2:
                for i in f1:
                    if username in i:
                        print("\033[0;35;0m用户名已经存在！请重新注册")
                        go_on = input("是否继续尝试Y/N：")
                        if go_on.upper() == "Y":
                            break
                        elif go_on.upper() == "N":
                            flag = False
                            break
                        else:
                            print("\033[0;31;0m请输入正确的字符！！！\033[0m")
                else:
                    f2.write("%s %s\n" % (username, second_password))
                    print("\033[0;35;0m注册成功！<%s> 已经自动登录！" % (username,))
                    user_status["user"] = username
                    user_status["status"] = True
                    return username


@wrapper_outer(run_log)
def article_page():
    """文章页面"""
    print("文章页面".center(60, "-"))


@wrapper_outer(run_log)
def logs_page():
    """日记页面"""
    print("日记页面".center(60, "-"))


@wrapper_outer(run_log)
def comment_page():
    """评论页面"""
    print("评论页面".center(60, "-"))


@wrapper_outer(run_log)
def collection_page():
    """收藏页面"""
    print("收藏页面".center(60, "-"))


@wrapper_outer(run_log)
def log_out():
    """注销"""
    if user_status["user"] and user_status["status"]:
        print("\033[0;31;0m%s 用户已经注销！\033[0m" % (user_status["user"]))
        user_status["user"] = None
        user_status["status"] = False
    else:
        print("\033[0;31;0m用户未登录!!!\033[0m")


@wrapper_outer(run_log)
def blog_exit():
    """退出"""
    print("\033[0;31;0mBye Bye!!!\033[0m".center(40, "-"))
    exit()


# user_status 用于存储用户状态
user_status = {"user": None, "status": False}
menu = {1: ['请登录', login],
        2: ['请注册', registered],
        3: ['文章页面', article_page],
        4: ['日记页面', logs_page],
        5: ['评论页面', comment_page],
        6: ['收藏页面', collection_page],
        7: ['注销', log_out],
        8: ['退出程序', blog_exit]}
print("\033[0;31;0m欢迎来到博客园首页\033[0m".center(60, " "))
while True:
    # 打印菜单
    print("-" * 64)
    for k, v in menu.items():
        print("\033[0;34;0m%s %s\033[0m" % (k, v[0]))
    print("-" * 64)
    choice = input("\n\033[0;36;0m请选择菜单：\033[0m").strip()
    if choice.isdigit():
        choice = int(choice)
        # 获取字典里面菜单key，如果不存在则返回1
        if menu.get(choice, 1) != 1:
            #  menu[choice][1]  = 字典里面存的函数命
            res = menu[choice][1]
            res()
        else:
            print("你输入的菜单ID不存在！")
    else:
        print("请输入正确的数字ID！")