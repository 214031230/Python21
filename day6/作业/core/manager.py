#!/usr/bin/env python3
class Manager:
    """管理员视图"""
    menus = {"1、创建学校": "",
             "2、创建班级": "",
             "3、创建课程": "",
             "4、创建讲师": "",
             "5、创建学员": ""}

    def __init__(self, name):
        self.name = name

    def create_school(self):
        pass

    def create_classes(self):
        pass

    def create_course(self):
        pass

    def create_teacher(self):
        pass

    def create_student(self):
        pass