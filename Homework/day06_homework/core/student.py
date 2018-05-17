#!/usr/bin/env python3
from conf.config import *
from core import my_json


class StudentManager:
    """学生视图"""
    menus = [["1、查看正在学习课程", "show_course"],
             ["2、查看所在班级", "show_classes"],
             ["3、退出", "manager_exit"]
             ]

    def __init__(self, name):
        self.name = name
        self.student_dic = my_json.load(studentinfo)

    def show_course(self):
        """
        查看学生所在班级
        :return:
        """
        for k, v in self.student_dic["course"].items():
            if self.name in v:
                print("正在学习：%s" % k)

    def show_classes(self):
        """
        查看学生所在班级
        :return:
        """
        for k, v in self.student_dic["classes"].items():
            if self.name in v:
                print("所在班级：%s" % k)

    def manager_exit(self):
        exit(self.name)


