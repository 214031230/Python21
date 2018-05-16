#!/usr/bin/env python3
class TeacherManager:
    """教师视图"""
    menus = [["1、查看授课班级", "show_classes"],
             ["2、查看授课科目", "show_course"],
             ["3、查看班级成员", "show_student"]
             ]

    def __init__(self, name):
        self.name = name

    def show_course(self):
        print("in show_course", self.name)

    def show_classes(self):
        print("in show_classes", self.name)

    def show_student(self):
        print("in show_student", self.name)
