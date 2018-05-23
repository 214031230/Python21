#!/usr/bin/env python3
from core.manager import Manager


class StudentManager:
    menus = [["1.查看所在班级", "show_classes"],
             ["2.查看所学课程", "show_course"],
             ["3.学生选择课程", "binding_course"],
             ["4.学生选择班级", "binding_classes"]
             ]

    def __init__(self, name):
        self.name = name

    def show_classes(self):
        obj = Manager(self.name)
        obj.show_student(self.name, "classes")

    def show_course(self):
        obj = Manager(self.name)
        obj.show_student(self.name, "course")

    def binding_course(self):
        pass

    def binding_classes(self):
        pass
