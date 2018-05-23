#!/usr/bin/env python3
from core.manager import Manager


class TeacherManager:
    menus = [["1.查看负责的班级", "show_classes"],
             ["2.查看负责课程", "show_course"],
             ["3.查看班级成员", "show_student"]]

    def __init__(self, name):
        self.name = name

    def show_classes(self):
        obj = Manager(self.name)
        obj.show_teacher(self.name, "classes")

    def show_course(self):
        obj = Manager(self.name)
        obj.show_teacher(self.name, "course")

    def show_student(self):
        pass
