#!/usr/bin/env python3
from core.manager import Manager
from core.public import *
from conf import settings


class TeacherManager:
    menus = [["1.查看负责的班级 ", "show_classes"],
             ["2.查看负责课程 ", "show_course"],
             ["3.老师选择课程 ", "binding_course"],
             ["4.老师选择班级 ", "binding_classes"],
             ["Q/q.退出 ", "sys_exit"]]

    def __init__(self, name):
        self.name = name
        self.log = Public.log()

    def show_classes(self):
        obj = Manager(self.name)
        obj.show_teacher(self.name, "classes")

    def show_course(self):
        obj = Manager(self.name)
        obj.show_teacher(self.name, "course")

    def binding_course(self):
        ret = Public.choice_classes_course(self.name, Manager, settings.teacherinfo, settings.courseinfo, "course","show_course")
        if ret == 1:Public.print("""
                        成功关联课程！！！
                        """)

    def binding_classes(self):
        ret = Public.choice_classes_course(self.name, Manager, settings.teacherinfo, settings.classinfo, "classes", "show_classes")
        if ret == 1:Public.print("""
                        成功关联班级！！！
                        """)

    def sys_exit(self):
        """程序退出"""
        self.log.info("%s 退出了程序" % self.name)
        exit()