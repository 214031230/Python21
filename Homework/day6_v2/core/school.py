#!/usr/bin/env python3
from core import my_pickle
from conf import config
from core.public import *


class School:
    def __init__(self, name, address, classes={}, course={}, teacher={}):
        """
        :param name: 学校名称
        :param address: 学校地址
        """
        self.name = name
        self.address = address
        self.course = course
        self.classes = classes
        self.teacher = teacher

    def create(self):
        """
        创建学校
        :return: 
        """
        ret = my_pickle.load(config.schoolinfo)
        if self.name in ret.keys():
            print_log("学校名已经存在！", "error")
            return
        ret[self.name] = self
        my_pickle.dump(ret, config.schoolinfo)
        print_log("""
                    创建学校<%s>成功!
                    学校名称：%s
                    学校地址：%s
                """ % (self.name, self.name, self.address))


class Classes:
    def __init__(self, name):
        """
        :param name: 班级名称
        """
        self.name = name

    def create(self, school):
        """
        创建班级
        :return: 
        """
        create_info(config.classinfo, school, self, "classes")
        print_log("""
                    创建班级<%s>成功!
                    班级名称：%s
                    所属学校：%s
                    """ % (self.name, self.name, school.name))


class Course:
    def __init__(self, name, moth, price):
        """
        :param name: 课程名称
        :param moth: 课程周期
        :param price: 课程价格
        """
        self.name = name
        self.moth = moth
        self.price = price

    def create(self, school):
        """
        创建课程
        :return: 
        """
        create_info(config.courseinfo, school, self, "course")
        print_log("""
                    创建课程<%s>成功!
                    课程名称：%s
                    课程周期：%s
                    课程价格：%s
                    开设学校：%s
                    """ % (self.name, self.name, self.moth, self.price, school.name), None)


class Person:
    def __init__(self, name, age="18", sex="女"):
        self.name = name
        self.age = age
        self.sex = sex


class Teacher(Person):
    def __init__(self, name, age="18", sex="女", school=None, course=None, classes=None):
        super().__init__(name)

    def create(self, school, course):
        create_info_user(config.teacherinfo, school, course, self)
        create_user(self.name, "TeacherManager")
        print_log("""
                    创建老师<%s>成功!
                    老师名称：%s
                    专业技能：%s
                    所属学校：%s
                    默认密码：123
                    """ % (self.name, self.name, course.name, school.name), None)

    def brond_classes(self, classes):
        self.classes[classes.name] = classes
        print("<%s>老师负责<%s>班级" % (self.name, classes.name))


class Student(Person):
    def __init__(self, name, age="18", sex="男", class_time=None):
        super().__init__(name)
        self.class_time = class_time

    def create(self, school, course):
        create_info_user(config.studentinfo, school, course, self)
        create_user(self.name, "StudentManager")
        print_log("""
                    创建学生<%s>成功!
                    学生名称：%s
                    所学课程：%s
                    所属学校：%s
                    默认密码：123
                    """ % (self.name, self.name, course.name, school.name), None)

    def brond_classes(self,classes):
        print("<%s>学生被分配到<%s>班级" % (self.name, classes.name))

    def brond_course(self, course):
        print("<%s>学生选择了<%s>课程" % (self.name, course.name))

