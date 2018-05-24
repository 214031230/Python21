#!/usr/bin/env python3
from core.public import MyPickle
from conf import settings
from core.public import *


class School:
    def __init__(self, name, num=0, classes={}, course={}, teacher={}, student={}):
        """
        :param name: 学校名称
        :param num: 学校的ID
        :param classes: 学校包含的所有班级
        :param course: 学校包含的所有课程
        :param teacher: 学校包含的所有老师
        :param student: 包含学校的所有学生
        """
        self.name = name
        self.num = num
        self.course = course
        self.classes = classes
        self.teacher = teacher
        self.student = student

    def create(self):
        """
        创建学校
        :return: 返回成功
        """
        ret = MyPickle.load(settings.schoolinfo)
        for i in ret.values():
            if self.name == i.name:
                Public.print("%s已经存在！" % self.name, "error")
                return 0
        self.num = len(ret) + 1
        ret[self.num] = self
        MyPickle.dump(ret, settings.schoolinfo)
        Public.print("""
                    Create<%s>Success!
                """ % self.name)
        return 1


class Classes:
    def __init__(self, name, num=0, teacher={}, student={}):
        """
        :param name: 班级名称
        :param num: 班级id
        :param teacher:班级有那老师
        :param student:班级有哪些学生
        """
        self.name = name
        self.num = num
        self.teacher = teacher
        self.student = student

    def create(self, school, file, types):
        """
        创建班级
        :param school: 学校对象
        :param file: 班级或者课程表
        :param types: 属性classes或者course
        :return: 0 = 名称已经存在
                  1 = 创建成功
        """
        ret = MyPickle.load(file)
        # for i in ret.values():
        #     if self.name == i.name:
        #         Public.print("%s已经存在！" % self.name, "error")
        #         return 0
        self.num = len(ret) + 1
        ret[self.num] = self
        MyPickle.dump(ret, file)
        Public.print("""
                    Create<%s>Success!
                    Name：%s
                """ % (self.name, self.name))

        ret = MyPickle.load(settings.schoolinfo)
        getattr(ret[school.num], types)[self.num] = self
        MyPickle.dump(ret, settings.schoolinfo)
        return 1


class Course(Classes):
    pass


class Teacher:
    def __init__(self, name, num=0, school="", course={}, classes={}):
        """
        :param name: 老师名称
        :param num: 老师ID
        :param school: 所属学校
        :param course: 所交课程{}
        :param classes: 所交班级{}
        """
        self.name = name
        self.num = num
        self.school = school
        self.course = course
        self.classes = classes

    def create(self, school_obj, file, types):
        """
        创建老师
        :param school_obj: 学校对象
        :param file : 文件
        :param types：属性 student或者teacher
        :return: 1 = 成功
                  0 = 已经存在
        """
        ret = MyPickle.load(file)
        for i in ret.values():
            if self.name == i.name:
                Public.print("%s已经存在！" % self.name, "error")
                return 0
        self.num = len(ret) + 1
        self.school = school_obj
        ret[self.num] = self
        MyPickle.dump(ret, file)
        Public.print("""
                    Create<%s>Success!
                    Name：%s
                    School：%s
                """ % (self.name, self.name, school_obj.name))

        ret = MyPickle.load(settings.schoolinfo)
        getattr(ret[school_obj.num], types)[self.num] = self
        MyPickle.dump(ret, settings.schoolinfo)
        return 1


class Student(Teacher):
    pass

