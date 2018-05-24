#!/usr/bin/env python3
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
        :return: 1 = 返回成功
                  0 = 学校已经存在
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


class SchoolInfo:
    def __init__(self, name, num=0):
        """
        :param name: 班级名称
        :param num: 班级id
        """
        self.name = name
        self.num = num

    def create(self, school, file, types):
        """
        创建班级
        :param school: 学校对象
        :param file: 班级或者课程表
        :param types: 属性classes或者course
        :return: 1 = 创建成功

        """
        ret = MyPickle.load(file)
        self.num = len(ret) + 1
        ret[self.num] = self
        MyPickle.dump(ret, file)
        Public.print("""
                    Create<%s>Success!
                    Name：%s
                    School：%s
                """ % (self.name, self.name, school.name))
        ret = MyPickle.load(settings.schoolinfo)
        getattr(ret[school.num], types)[self.num] = self
        MyPickle.dump(ret, settings.schoolinfo)
        return 1


class Classes(SchoolInfo):
    pass


class Course(SchoolInfo):
    pass


class User:
    def __init__(self, name, num=0, school="", course={}, classes={}):
        """
        :param name: 老师、学生名称
        :param num: 老师、学生ID
        :param school: 所属学校 一个老师、学生只能属于一所学校
        :param course: 老师、学生可以有多个课程{}
        :param classes: 老师、学生可以有多个班级{}
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
        :param file : 学生或者老师表
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


class Teacher(User):
    pass


class Student(User):
    pass

