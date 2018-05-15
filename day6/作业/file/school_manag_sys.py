#!/usr/bin/env python3
import json
user_status = {"user": None, "status": False}


def registered():
    """
    创建用户
    :return:
    """
    print_log(">>>创建用户:")
    flag = True
    while flag:
        user = input("\033[0;35;0m请输入昵称：").strip()
        username = input("\033[0;35;0m请输入用户名：").strip()
        password = input("\033[0;35;0m请输入密码：").strip()
        usertype = input("\033[0;35;0m请输入用户类型：").strip()
        if not usertype: usertype = "student"
        if user and username and password:
            spf = User(user, username, password, usertype)
            spf.add_user()
        else:
            print_log("ERROR:昵称/用户名/密码不能为空", "error")


def login():
    """
    用户登录
    :return: 登录成功返回teacher  student admin
    """
    print_log(">>欢迎登录：")
    count = 0
    while count < 3:
        username = input("\033[0;35;0m请输入用户名：\033[0m").strip()
        password = input("\033[0;35;0m请输入密码：\033[0m").strip()
        if not username or not password:
            print_log("ERROR:用户名或密码不能为空", "error")
        user_info = tab_load("user_info")
        if username in user_info["username"]:
            pwd_index = user_info["username"].index(username)
            if password == user_info["password"][pwd_index]:
                if user_info["usertype"][pwd_index] == "teacher":
                    return "teacher"
                elif user_info["usertype"][pwd_index] == "admin":
                    return "admin"
                elif user_info["usertype"][pwd_index] == "student":
                    return "student"
            else:
                print_log("ERROR：密码错误", "error")
        else:
            print_log("ERROR：用户名不存在", "error")
        count += 1


def print_log(meg, type="info"):
    """
    输出信息变色，info：蓝色。error：红色
    :param meg: 需要变色的信息
    :param type: 信息类型
    :return:
    """
    if type == "info":
        print("\033[36;0m%s\033[0m" % meg)
    if type == "error":
        print("\033[36;0m%s\033[0m" % meg)


def tab_dump(dic, t_name):
    """
    把字典序列化到内存中
    :param dic: 字典，存储表数据
    :param t_name:  表名称
    :return:
    """
    f = open("./db/%s" % t_name, mode="w")
    json.dump(dic, f)
    f.close()


def tab_load(t_name):
    """
    把表内容反序列化成字典
    :param t_name: 表名称
    :return: 返回一个字典
    """
    f = open("./db/%s" % t_name)
    dic = json.load(f)
    f.close()
    return dic


def init_table(t_name,dic):
    """
    初始化表
    :param t_name:  表名
    :param dic: 表结构
    :return:
    """
    try:
        tab_load(t_name)
    except json.decoder.JSONDecodeError:
        user_info = dic
        tab_dump(user_info, t_name)

class User:
    """
    用户管理类
    """
    def __init__(self, user, username, password, usertype):
        """
        用户的基本属性
        :param name:  昵称
        :param username: 唯一用户名
        :param password: 密码
        :param usertype: 用户类型teacher student admin
        """
        self.user = user
        self.username = username
        self.password = password
        self.usertype = usertype

    def add_user(self):
        """
        创建用户
        :return:
        """

        user_info = {"user": [], "username": [], "password": [], "usertype": []}
        init_table("user_info",user_info)
        user_info = tab_load("user_info")
        if self.username in user_info["user"]:
            print_log("ERROR:用户已经存在", "error")
            return
        user_info["user"].append(self.user)
        user_info["username"].append(self.username)
        user_info["password"].append(self.password)
        user_info["usertype"].append(self.usertype)
        tab_dump(user_info, "user_info")


class School:
    """
    学校管理
    """
    def __init__(self, school_name, school_city):
        """
        学校属性
        :param school_name:  学校名称
        :param school_city: 学校所属城市
        """
        self.school_name = school_name
        self.school_city = school_city

    def add_school(self):
        """
        创建学校
        :return:
        """
        school_info = {"name": [], "city": []}
        init_table("school_info",school_info)
        school_info = tab_load("school_info")
        if self.school_name in school_info["name"]:
            print_log("ERROR:学校名经存在", "error")
            return
        school_info["name"].append(self.school_name)
        school_info["city"].append(self.school_city)
        tab_dump(school_info, "school_info")

class Classroom:
    """
    班级管理
    """
    def __init__(self,class_name):
        """
        班级属性
        :param class_name: 班级名称
        """
        self.class_name = class_name

    def add_classroom(self):
        """
        创建班级
        :return:
        """



def user_view(user):
    """
    视图
    :param user: 用户类型  admin teacher  student
    :return:
    """
    if user == "admin":
        print_log("""
        1、创建学校
        2、创建班级
        3、创建课程
        4、创建讲师
        5、创建学员
        6、查看学校
        """)
        while True:
            choice = input(">>>:").strip()
            if not choice:continue
            if choice == "1":
                school_name = input("请输入学校名称：").strip()
                school_city = input("请输入学校所属城市：").strip()
                if not school_name and not school_city: continue
                school = School(school_name, school_city)
                school.add_school()
            elif choice == "6":
                ret = tab_load("school_info")
                print_log(ret)
            elif choice == "2":
                pass



    elif user == "teacher":
        print_log("""
        1、查看班级学员
        2、查看学员成绩
        2、修改学员成绩
        """)
    elif user == "student":
        print_log("""
        1、查看成绩
        2、查看课程
        """)

if __name__ == "__main__":
    print_log("校园管理系统".center(50, "-"))
    ret = login()
    user_view(ret)



