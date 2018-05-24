#!/usr/bin/env python3
from core.manager import Manager
from core.public import *


class StudentManager:
    menus = [["1.查看所在班级 ", "show_classes"],
             ["2.查看所学课程 ", "show_course"],
             ["3.学生选择课程 ", "binding_course"],
             ["4.学生选择班级 ", "binding_classes"],
             ["Q/q.退出 ", "sys_exit"]]

    def __init__(self, name):
        """
        :param name: 学生账号
        """
        self.name = name
        self.log = Public.log()

    def show_classes(self):
        """查看班级"""
        obj = Manager(self.name)
        obj.show_student(self.name, "classes")

    def show_course(self):
        """查看课程"""
        obj = Manager(self.name)
        obj.show_student(self.name, "course")

    def binding_course(self):
        """关联课程"""
        ret = Public.choice_classes_course(self.name, Manager, settings.studentinfo,
                                           settings.courseinfo, "course", "show_course")
        if ret == 1:Public.print("""
                        成功关联课程！！！
                        """)

    def binding_classes(self):
        """关联班级"""
        ret = Public.choice_classes_course(self.name, Manager, settings.studentinfo,
                                           settings.classinfo, "classes", "show_classes")
        if ret == 1:Public.print("""
                        成功关联班级！！！
                        """)

    def sys_exit(self):
        """程序退出"""
        self.log.info("%s 退出了程序" % self.name)
        exit()
