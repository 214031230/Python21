#!/usr/bin/env python3


def wrapper(argv):
    """登录"""
    def inner():
        if user_status["user"] != None and user_status["status"] != False:
            argv()
        else:
            print("\033[0;32;0m\n>>>欢迎登录：")
            count = 0
            while count < 3:
                username = input("\033[0;32;0m请输入用户名：\033[0m").strip()
                password = input("\033[0;32;0m请输入密码：\033[0m").strip()
                if not username or not password:
                    print("\033[0;32;0m用户名或密码不能为空\033[0m")
                with open("./file/user_list") as f1:
                    for i in f1:
                        user, passwd = i.split()
                        if username == user and password == passwd:
                            print("\033[0;32;0m登录成功！\n\033[0;32;0m")
                            user_status["user"] = username
                            user_status["status"] = True
                            return username
                    else:
                        print("\033[0;32;0m用户名或者密码错误，请重试！\033[0m")
                count += 1
            else:
                exit()
    return inner


@wrapper
def login():
    print("欢迎登录！")


def registered():
    """注册"""
    print("\033[0;32;0m\n>>>欢迎注册:")
    while True:
        username = input("\033[0;32;0m请输入用户名：").strip()
        first_password = input("\033[0;32;0m请输入密码：").strip()
        second_password = input("\033[0;32;0m请确认密码：").strip()

        if not username or not first_password or not second_password:
            print("\033[0;32;0m用户名或者密码不能为空！")
            continue

        if first_password != second_password:
            print("\033[0;32;0m两次密码输入不一致，请重新输入！")
            continue

        with open("./file/user_list", mode="r") as f1, open("./file/user_list", mode="a") as f2:
            for i in f1:
                if username in i:
                    print("\033[0;32;0m用户名已经存在！请重新注册")
                    break
            else:
                f2.write("%s %s\n" % (username, second_password))
                print("\033[0;32;0m注册成功！")
                user_status["user"] = username
                user_status["status"] = True
                return username
            

@wrapper
def article_page():
    """文章页面"""
    print("""\033[0;33;0m文章页面
            咏鹅
    
            鹅鹅鹅，
            曲项向天歌。
            白毛浮绿水，
            红掌拨清波。
            """.center(50," "))


@wrapper
def logs_page():
    """日记页面"""
    print("日志页面！")


@wrapper
def comment_page():
    """评论页面"""
    print("评论页面")


@wrapper
def collection_page():
    """收藏页面"""
    print("收藏页面")


def log_out():
    """注销"""
    user_status["user"] = None
    user_status["status"] = False


def blog_exit():
    """退出"""
    return False


user_status = {"user": None, "status": False}

menu = {1: '请登录',
        2: '请注册',
        3: '文章页面',
        4: '日记页面',
        5: '评论页面',
        6: '收藏页面',
        7: '注销',
        8: '退出程序'}
flag = True
print("\033[0;31;0m欢迎来到博客园首页\033[0m".center(60, " "))
while flag:
    for k, v in menu.items():
        print("\033[0;34;0m%s %s\033[0m" % (k, v))
    choice = input("\n\033[0;36;0m请选择菜单：\033[0m")
    if choice == "1":
        login()
    elif choice == "2":
        registered()
    elif choice == "3":
        article_page()
    elif choice == "4":
        logs_page()
    elif choice == "5":
        comment_page()
    elif choice == "6":
        collection_page()
    elif choice == "7":
        log_out()
    elif choice == "8":
        flag = blog_exit()
