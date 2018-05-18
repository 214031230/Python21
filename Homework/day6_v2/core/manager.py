#!/usr/bin/env python3
from core.school import *
from core.my_pickle import MyPickle
from conf import config

class Manager:
    menus = [["1、创建学校", "create_school"],
             ["             2、查看学校", "show_school"],
             ["3、创建班级", "create_classes"],
             ["             4、查看班级", "show_classes"],
             ["5、创建课程", "create_course"],
             ["             6、查看课程", "show_course"],
             ["7、创建讲师", "create_teacher"],
             ["             8、查看讲师", "show_teacher"],
             ["9、创建学员", "create_student"],
             ["             10、查看学员", "show_student"],
             ["11、初始化数据库", "init_db"],
             ["             12、退出", "manager_exit"]
             ]

    def __init__(self, name):
        self.name = name
        self.school_tab = MyPickle(config.schoolinfo)

    def create_school(self):
        name = input(">>>请输入学校名称：")
        addr = input(">>>请输入学校地址：")
        obj = School(name, addr)
        obj.create()

    def show_school(self):
        ret = self.school_tab.load()
        for i in ret.values():
            print(i.__dict__)

