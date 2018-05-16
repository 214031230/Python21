#!/usr/bin/env python3
import json
from sys import modules
userinfo = "./db/user_info"
schoolinfo = "./db/school_info"
classinfo = "./db/class_info"
couresinfo = "./db/coures_info"
teacherinfo  = "./db/teacher_info"
studentinfo = "./db/student_info"


def init_db():
    """
    初始化数据库
    :return:
    """
    userinfo_dic = {"username": ["admin"], "password": ["123"], "usertype": ["Manager"]}
    schoolinfo_dic = {"name": [], "city": []}
    classinfo_dic = {"name": {}, "s_name": [], "course": [], "student": []}
    couresinfo_dic = {"name": {}, "s_name": [], "month": [], "price": []}
    teacherinfo_dic = {"name": [], "s_name":[], "classes": {}, "course": {}}
    studentinfo_dic = {"name": [], "s_name":[], "classes": [], "course": []}
    tab_dump(userinfo_dic, userinfo)
    tab_dump(schoolinfo_dic, schoolinfo)
    tab_dump(couresinfo_dic, couresinfo)
    tab_dump(classinfo_dic, classinfo)
    tab_dump(teacherinfo_dic, teacherinfo)
    tab_dump(studentinfo_dic, studentinfo)


class Manager:
    """管理员视图"""
    menus = [["1、创建学校", "create_school"],
             ["2、创建班级", "create_classes"],
             ["3、创建课程", "create_course"],
             ["4、创建讲师", "create_teacher"],
             ["5、创建学员", "create_student"],
             ["6、初始化数据库", "init_db"]
             ]

    def __init__(self, name):
        self.name = name

    def create_school(self):
        while True:
            name = input("请输入学校名：").strip()
            city = input("请输入学校所在城市：").strip()
            obj = School(name, city)
            ret = tab_load(schoolinfo)
            if obj.name in ret["name"]:
                print("ERROR：学校名已存在")
                continue
            ret["name"].append(obj.name)
            ret["city"].append(obj.city)
            tab_dump(ret, schoolinfo)
            print("""
                    创建学校成功：
                    学校名称：%s
                    所在城市：%s
            """ % (obj.name, obj.city))
            break

    def create_classes(self):
        while True:
            ret = tab_load(schoolinfo)
            if len(ret["name"]) == 0:
                print("ERROR：请先创建学校！")
                break
            for index, i in enumerate(ret["name"], 1):
                print(index, i)
            school = input("请选择学校：").strip()
            course_dic = tab_load(couresinfo)
            if len(course_dic["name"]) == 0:
                print("ERROR：请先创课程！")
                break
            for index, i in enumerate(course_dic["name"][ret["name"][int(school) - 1]], 1):
                print(index, i)
            course = input("请选择班级课程：").strip()
            name = input("请输入班名名称：").strip()
            obj = Classes(name, ret["name"][int(school) - 1], course_dic["name"][ret["name"][int(school) - 1]][int(course) - 1])
            ret_dic = tab_load(classinfo)
            ret_dic["s_name"].append(obj.school)
            if not ret_dic["name"].get(obj.school):
                ret_dic["name"][obj.school] = []
            ret_dic["name"][obj.school].append(obj.name)
            ret_dic["course"].append(obj.course)
            tab_dump(ret_dic, classinfo)
            print("""
                    创建班级成功：
                    班级名称：%s
                    所在学校：%s
                    班级科目：%s
            """ % (obj.name, obj.school, obj.course))
            break

    def create_course(self):
        while True:
            ret = tab_load(schoolinfo)
            if len(ret["name"]) == 0:
                print("ERROR：请先创建学校！")
                break
            for index, i in enumerate(ret["name"], 1):
                print(index, i)
            school = input("请选择学校：").strip()
            name = input("请输课程名称：").strip()
            month = input("请输入课程周期：").strip()
            price = input("请输入课程价格：").strip()
            obj = Course(name, ret["name"][int(school) - 1], month, price)
            ret_dic = tab_load(couresinfo)
            ret_dic["s_name"].append(ret["name"][int(school) - 1])
            if not ret_dic["name"].get(obj.school):
                ret_dic["name"][obj.school] = []
            ret_dic["name"][obj.school].append(obj.name)
            ret_dic["month"].append(obj.month)
            ret_dic["price"].append(obj.price)
            tab_dump(ret_dic, couresinfo)
            print("""
                    创建课程成功：
                    授课学校：%s
                    课程名称：%s
                    课程周期：%s
                    课程价格：%s
            """ % (obj.school, obj.name, obj.month, obj.price))
            break

    def create_teacher(self):
        while True:
            ret = tab_load(schoolinfo)
            if len(ret["name"]) == 0:
                print("ERROR：请先创建学校！")
                break
            for index, i in enumerate(ret["name"], 1):
                print(index, i)
            school = input("请选择学校：").strip()
            course_dic = tab_load(couresinfo)
            if len(course_dic["name"]) == 0:
                print("ERROR：请先创课程！")
                break
            for index, i in enumerate(course_dic["name"][ret["name"][int(school) - 1]], 1):
                print(index, i)
            course = input("请选择老师授课科目：").strip()
            classes_dic = tab_load(classinfo)
            if len(classes_dic["name"]) == 0:
                print("ERROR：请先创建班级！")
                break
            for index, i in enumerate(classes_dic["name"][ret["name"][int(school) - 1]], 1):
                print(index, i)
            classes = input("请选择老师授课班级：").strip()
            name = input("请输入老师账号：").strip()
            pwd = input("请输入账号密码：").strip()
            user_dic = tab_load(userinfo)
            user_dic["username"].append(name)
            user_dic["password"].append(pwd)
            user_dic["usertype"].append("TeacherManager")
            tab_dump(user_dic, userinfo)
            obj = Teacher(name, ret["name"][int(school) - 1], classes_dic["name"][ret["name"][int(school) - 1]][int(classes) - 1], course_dic["name"][ret["name"][int(school) - 1]][int(course) - 1])
            teacher_dic = tab_load(teacherinfo)
            teacher_dic["name"].append(obj.name)
            teacher_dic["s_name"].append(obj.school)
            if not teacher_dic["classes"].get(obj.name):
                teacher_dic["classes"][obj.name] = []
            teacher_dic["classes"][obj.name].append(obj.classes)
            if not teacher_dic["course"].get(obj.name):
                teacher_dic["course"][obj.name] = []
            teacher_dic["course"][obj.name].append(obj.course)
            tab_dump(teacher_dic, teacherinfo)
            print("""
                    创建老师成功：
                    老师账号：%s
                    所在学校：%s
                    授课班级：%s
                    授课科目：%s
            """ % (obj.name, obj.school, obj.classes, obj.course))
            break

    def create_student(self):
        while True:
            ret = tab_load(schoolinfo)
            if len(ret["name"]) == 0:
                print("ERROR：请先创建学校！")
                break
            for index, i in enumerate(ret["name"], 1):
                print(index, i)
            school = input("请选择学校：").strip()
            course_dic = tab_load(couresinfo)
            if len(course_dic["name"]) == 0:
                print("ERROR：请先创课程！")
                break
            for index, i in enumerate(course_dic["name"][ret["name"][int(school) - 1]], 1):
                print(index, i)
            course = input("请选择课程：").strip()
            classes_dic = tab_load(classinfo)
            if len(classes_dic["name"]) == 0:
                print("ERROR：请先创建班级！")
                break
            # for index, i in enumerate(classes_dic["name"], 1):
            for index, i in enumerate(classes_dic["name"][ret["name"][int(school) - 1]], 1):

                print(index, i)
            classes = input("请选择班级：").strip()
            name = input("请输入学生账号：").strip()
            pwd = input("请输入学生密码：").strip()
            user_dic = tab_load(userinfo)
            user_dic["username"].append(name)
            user_dic["password"].append(pwd)
            user_dic["usertype"].append("StudentManager")
            tab_dump(user_dic, userinfo)
            obj = Student(name, ret["name"][int(school) - 1], classes_dic["name"][ret["name"][int(school) - 1]][int(classes) - 1], course_dic["name"][ret["name"][int(school) - 1]][int(course) - 1])
            Student_dic = tab_load(studentinfo)
            Student_dic["name"].append(obj.name)
            Student_dic["s_name"].append(obj.school)
            Student_dic["classes"].append(obj.classes)
            Student_dic["course"].append(obj.course)
            tab_dump(Student_dic, studentinfo)
            print("""
                    创建老师成功：
                    学生账号：%s
                    所在学校：%s
                    所在班级：%s
                    所学课程：%s
            """ % (obj.name, obj.school, obj.classes, obj.course))
            break

    def init_db(self):
        init_db()


class StudentManager:
    """学生视图"""
    menus = [["1、查看正在学习课程", "show_course"],
             ["2、查看所在班级", "show_classes"],
             ]

    def __init__(self, name):
        self.name = name

    def show_course(self):
        ret = tab_load(studentinfo)
        index = ret["name"].index(self.name)
        print(ret["course"][index])

    def show_classes(self):
        ret = tab_load(studentinfo)
        index = ret["name"].index(self.name)
        print(ret["classes"][index])


class TeacherManager:
    """教师视图"""
    menus = [["1、查看授课班级", "show_classes"],
             ["2、查看授课科目", "show_course"],
             ]

    def __init__(self, name):
        self.name = name

    def show_course(self):
        ret = tab_load(teacherinfo)
        for i in ret["course"][self.name]:
            print(i)

    def show_classes(self):
        ret = tab_load(teacherinfo)
        for i in ret["classes"][self.name]:
            print(i)


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
    f = open(t_name, mode="w")
    json.dump(dic, f)
    f.close()


def tab_load(t_name):
    """
    把表内容反序列化成字典
    :param t_name: 表名称
    :return: 返回一个字典
    """
    f = open(t_name)
    dic = json.load(f)
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
