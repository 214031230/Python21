#!/usr/bin/env python3
import pickle
from sys import modules
userinfo = "./db/user_info"
schoolinfo = "./db/school_info"
classinfo = "./db/class_info"
couresinfo = "./db/coures_info"
teacherinfo  = "./db/teacher_info"
studentinfo = "./db/student_info"


class Manager:
    """管理员视图"""
    menus = [["1、创建学校", "create_school"],
             ["2、创建班级", "create_classes"],
             ["3、创建课程", "create_course"],
             ["4、创建讲师", "create_teacher"],
             ["5、创建学员", "create_student"],
             ]

    def __init__(self, name):
        self.name = name

    def create_school(self):
        pass

    def create_classes(self):
        pass

    def create_course(self):
        pass

    def create_teacher(self):
        pass

    def create_student(self):
        pass



class StudentManager:
    """学生视图"""
    menus = [["1、查看正在学习课程", "show_course"],
             ["2、查看所在班级", "show_classes"],
             ]

    def __init__(self, name):
        self.name = name

    def show_course(self):
        pass

    def show_classes(self):
        pass


class TeacherManager:
    """教师视图"""
    menus = [["1、查看授课班级", "show_classes"],
             ["2、查看授课科目", "show_course"],
             ]

    def __init__(self, name):
        self.name = name

    def show_course(self):
        pass

    def show_classes(self):
        pass


class School:
    def __init__(self, name, city):
        """
        :param name: 学校名称
        :param city: 学校所在城市
        """
        self.name = name
        self.city = city


class Teacher:
    def __init__(self, name, school, classes=None, course=None):
        """
        :param name: 老师账号
        :param school: 学校对象
        :param classes: 班级对象
        :param course: 课程对象
        """
        self.name = name
        self.school = school
        self.classes = classes
        self.course = course


class Student:
    def __init__(self, name, school, classes, course):
        """
        :param name: 学员账号
        :param school: 学校对象
        :param classes: 班级对象
        :param course: 课程对象
        """
        self.name = name
        self.school = school
        self.classes = classes
        self.course = course


class Classes:
    def __init__(self, name, school, course, student=[]):
        """
        :param name: 班级名称 例如 python21期
        :param school: 学校对象
        :param course: 课程对象 例如python
        :param student: 学生对象
        """
        self.name = name
        self.school = school
        self.course = course
        self.student = student


class Course:
    """课程管理"""
    def __init__(self, name, school, month, price):
        """
        :param name: 课程名称
        :param school: 课程开设学校
        :param month: 课程周期 例如6个月
        :param price: 课程价格
        """
        self.name = name
        self.school = school
        self.month = month
        self.price = price


def tab_dump(dic, t_name):
    """
    把字典序列化到内存中
    :param dic: 字典，存储表数据
    :param t_name:  表名称
    :return:
    """
    f = open(t_name, mode="wb")
    pickle.dump(dic, f)
    f.close()


def tab_load(t_name):
    """
    把表内容反序列化成字典
    :param t_name: 表名称
    :return: 返回一个字典
    """
    f = open(t_name, "rb")
    dic = pickle.load(f)
    f.close()
    return dic


def login():
    """
    用户登录
    :return: 登录成功返回用户名和身份teacher  student admin
    """
    print("\033[0;31;0m欢迎访问老男孩管理系统".center(50, "-"))
    print(">>>请登录：\033[0m")
    count = 0
    while count < 3:
        username = input("\033[0;35;0m请输入用户名：\033[0m").strip()
        password = input("\033[0;35;0m请输入密码：\033[0m").strip()
        if not username or not password:
            print("ERROR:用户名或密码不能为空")
        user_info = tab_load(userinfo)
        if username in user_info["username"]:
            pwd_index = user_info["username"].index(username)
            if password == user_info["password"][pwd_index]:
                return username, user_info["usertype"][pwd_index]
            else:
                print("ERROR：密码错误")
        else:
            print("ERROR：用户名不存在")
        count += 1


def main():
    """
    选择视图
    通过对象角色去调用对应的方法，根据用户选择跳转到对应的方法中
    :return:
    """
    ret = login()
    while True:
        if ret:
            role_class = getattr(modules[__name__], ret[1])
            obj = role_class(ret[0])
            for i in obj.menus:
                print(i[0])
            choice = input("请选择功能：").strip()
            func = obj.menus[int(choice) - 1][1]
            getattr(obj, func)()


if __name__ == "__main__":
    main()

