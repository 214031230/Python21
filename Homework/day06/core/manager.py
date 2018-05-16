#!/usr/bin/env python3
from conf import config
from core import my_json


class Manager:
    """管理员视图"""
    menus = [["1、创建学校", "create_school"],
             ["2、查看学校", "show_school"],
             ["3、创建班级", "create_classes"],
             ["4、查看班级", "show_classes"],
             ["5、创建课程", "create_course"],
             ["6、查看课程", "show_course"],
             ["7、创建讲师", "create_teacher"],
             ["8、查看讲师", "show_teacher"],
             ["9、创建学员", "create_student"],
             ["10、查看学员", "show_student"],
             ["11、初始化数据库", "init_db"],
             ["12、退出", "manager_exit"]
             ]

    def __init__(self, name):
        self.name = name

    def create_school(self):
        print("in create_school", self.name)

    def show_school(self):
        print("in show_school", self.name)

    def create_classes(self):
        print("in create_classes", self.name)

    def show_classes(self):
        print("in show_classes", self.name)

    def create_course(self):
        print("in create_course", self.name)

    def show_course(self):
        print("in show_course", self.name)

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
        schoolinfo_dic = {"name": [], "city": []}
        classinfo_dic = {"name": {}, "s_name": [], "course": [], "student": []}
        couresinfo_dic = {"name": {}, "s_name": [], "month": [], "price": []}
        teacherinfo_dic = {"name": [], "s_name": [], "classes": {}, "course": {}}
        studentinfo_dic = {"name": [], "s_name": [], "classes": [], "course": []}
        my_json.dump(userinfo_dic, config.userinfo)
        my_json.dump(schoolinfo_dic, config.schoolinfo)
        my_json.dump(couresinfo_dic, config.couresinfo)
        my_json.dump(classinfo_dic, config.classinfo)
        my_json.dump(teacherinfo_dic, config.teacherinfo)
        my_json.dump(studentinfo_dic, config.studentinfo)

    def manager_exit(self):
        exit(self.name)
