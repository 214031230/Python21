#!/usr/bin/env python3
class StudentManager:
    """学生视图"""
    menus = [["1、查看正在学习课程", "show_course"],
             ["2、查看所在班级", "show_classes"],
             ]

    def __init__(self, name):
        self.name = name

    def show_course(self):
        print("in show_course", self.name)

    def show_classes(self):
        print("in show_classes", self.name)


