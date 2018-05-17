#!/usr/bin/env python3
from conf.config import *
from core import my_json


class TeacherManager:
    """教师视图"""
    menus = [["1、查看授课班级", "show_classes"],
             ["2、查看授课科目", "show_course"],
             ["3、查看班级成员", "show_student"],
             ["4、退出", "manager_exit"]
             ]

    def __init__(self, name):
        self.name = name
        self.teacher_dic = my_json.load(teacherinfo)

    def show_course(self):
        """
        查看课程
        :return:
        """
        print(self.teacher_dic["course"].get(self.name))

    def show_classes(self):
        """
        查看授课班级
        :return:
        """
        print(self.teacher_dic["classes"].get(self.name))

    def show_student(self):
        print("in show_student", self.name)

    def manager_exit(self):
        exit(self.name)
