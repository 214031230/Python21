#!/usr/bin/env python3
from conf.config import *
from core import my_json
from core.school import *
from tabulate import tabulate


class Manager:
    """管理员视图"""
    menus = [["1、创建学校", "create_school"],
             ["            2、查看学校", "show_school"],
             ["3、创建班级", "create_classes"],
             ["            4、查看班级", "show_classes"],
             ["5、创建课程", "create_course"],
             ["            6、查看课程", "show_course"],
             ["7、创建讲师", "create_teacher"],
             ["            8、查看讲师", "show_teacher"],
             ["9、创建学员", "create_student"],
             ["            10、查看学员", "show_student"],
             ["11、初始化数据库", "init_db"],
             ["12、退出", "manager_exit"]
             ]

    def __init__(self, name):
        self.name = name
        self.school_dic = my_json.load(schoolinfo)
        self.classes_dic = my_json.load(classinfo)
        self.student_dic = my_json.load(studentinfo)
        self.coures_dic = my_json.load(couresinfo)
        self.teacher_dic = my_json.load(teacherinfo)
        self.userinfo_dic = my_json.load(userinfo)

    def create_school(self):
        """
        创建学校
        :return:
        """
        print("in create_school", self.name)
        name = input(">>>请输入学校名称：").strip()
        city = input(">>>请输入所在城市：").strip()
        if name in self.school_dic["name"]:
            print("ERROR: 学校已经存在")
            return
        global school_obj
        school_obj = School(len(self.school_dic["name"]) + 1, name, city)
        self.school_dic["id"].append(school_obj.sid)
        self.school_dic["name"].append(school_obj.name)
        self.school_dic["city"].append(school_obj.city)
        my_json.dump(self.school_dic, schoolinfo)
        print("\033[0;31;0mINFO：创建成功\033[0m")

    def show_school(self):
        """
        查看学校
        :return:
        """
        schoolinfo_title = ["ID", "学校名称", "所属城市"]
        print("\033[1;31;0m")
        print(tabulate(self.school_dic, tablefmt="grid", headers=schoolinfo_title))
        print("\033[0m")

    def create_classes(self):
        """
        创建班级，创建班级前必须有学校
        :return:
        """
        if len(self.school_dic["id"]) == 0:
            print("ERROR：请先创建学校")
            return
        self.show_school()
        school = int(input(">>>请选择学校ID：").strip())
        name = input(">>>请输入班级名称：").strip()
        classes_obj = Classes(name, self.school_dic["name"][school - 1])
        if not self.classes_dic["name"].get(classes_obj.school):
            self.classes_dic["name"][classes_obj.school] = []
        self.classes_dic["name"][classes_obj.school].append(classes_obj.name)
        my_json.dump(self.classes_dic, classinfo)

    def show_classes(self, s_name=None):
        """
        查看班级
        :param s_name: 学校名称
        :return:
        """
        if s_name == None:
            for k in self.classes_dic["name"]:
                count = 1
                print("\033[1;31;0m学校：%s" % k)
                print("   班级：")
                for i in self.classes_dic["name"][k]:
                    print("\033[1;31;0m       %s.%s\033[0m" % (count, i))
                    count += 1
        else:
            count = 1
            print("\033[1;31;0m学校：%s" % s_name)
            print("   班级：")
            for k in self.classes_dic["name"][s_name]:
                print("\033[1;31;0m       %s.%s\033[0m" % (count, k))
                count += 1

    def create_course(self):
        """
        创建课程必须先选择学校，在选择班级
        :return:
        """
        if len(self.school_dic["id"]) == 0:
            print("ERROR：请先创建学校")
            return
        self.show_school()
        school = int(input(">>>请选择学校ID：").strip())
        name = input(">>>请输入课程名称：").strip()
        course_obj = Course(name, self.school_dic["name"][school - 1])
        if not self.coures_dic["name"].get(course_obj.school):
            self.coures_dic["name"][course_obj.school] = []
        self.coures_dic["name"][course_obj.school].append(course_obj.name)
        my_json.dump(self.coures_dic, couresinfo)
        # name = input(">>>请输入课程名称：").strip()
        # # self.show_classes(self.school_dic["name"][school - 1])

    def show_course(self, s_name=None):
        """
        查看课程
        :param s_name: 学校名称
        :return:
        """
        if s_name == None:
            for k in self.coures_dic["name"]:
                count = 1
                print("\033[1;31;0m学校：%s" % k)
                print("   课程：")
                for i in self.coures_dic["name"][k]:
                    print("\033[1;31;0m       %s.%s\033[0m" % (count, i))
                    count += 1
        else:
            count = 1
            print("\033[1;31;0m学校：%s" % s_name)
            print("   课程：")
            for k in self.coures_dic["name"][s_name]:
                print("\033[1;31;0m       %s.%s\033[0m" % (count, k))
                count += 1

    def create_teacher(self):
        print("in create_teacher", self.name)

    def show_teacher(self):
        print("in show_teacher", self.name)

    def create_student(self):
        print("in create_student", self.name)

    def show_student(self):
        print("in show_student", self.name)

    def init_db(self):
        userinfo_dic = {"username": ["admin"], "password": ["123"], "usertype": ["Manager"]}
        schoolinfo_dic = {"id": [], "name": [], "city": []}
        # classinfo_dic = {"name": {}, "s_name": [], "course": [], "student": []}
        classinfo_dic = {"name": {}}
        # couresinfo_dic = {"name": {}, "s_name": [], "month": [], "price": []}
        couresinfo_dic = {"name": {}}
        teacherinfo_dic = {"name": {}, "s_name": [], "classes": {}, "course": {}}
        studentinfo_dic = {"name": [], "s_name": [], "classes": [], "course": []}
        my_json.dump(userinfo_dic, userinfo)
        my_json.dump(schoolinfo_dic, schoolinfo)
        my_json.dump(couresinfo_dic, couresinfo)
        my_json.dump(classinfo_dic, classinfo)
        my_json.dump(teacherinfo_dic, teacherinfo)
        my_json.dump(studentinfo_dic, studentinfo)
        print("INFO:初始化成功")

    def manager_exit(self):
        exit(self.name)
