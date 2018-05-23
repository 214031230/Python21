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
        :return:
        """
        ret = MyPickle.load(file)
        for i in ret.values():
            if self.name == i.name:
                Public.print("%s已经存在！" % self.name, "error")
                return
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
    # def __init__(self, name, num=0):
    #     """
    #     :param name: 课程名称
    #     """
    #     self.name = name
    #     self.num = num

    # def create(self, school):
    #     """
    #     创建课程
    #     :return:
    #     """
    #     ret = MyPickle.load(settings.courseinfo)
    #     for i in ret.values():
    #         if self.name == i.name:
    #             Public.print("课程名已经存在！", "error")
    #             return
    #     self.num = len(ret) + 1
    #     ret[self.num] = self
    #     MyPickle.dump(ret, settings.courseinfo)
    #     Public.print("""
    #                 创建课程<%s>成功!
    #                 课程名称：%s
    #             """ % (self.name, self.name))
    #
    #     ret = MyPickle.load(settings.schoolinfo)
    #     ret[school.num].course[self.num] = self
    #     MyPickle.dump(ret, settings.schoolinfo)


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

    def create(self, school_obj, classes_obj, course_obj, file, types):
        """
        创建老师
        :param school_obj: 学校对象
        :param classes_obj: 班级对象
        :param course_obj: 课程对象
        :param file : 文件
        :param types：属性 student或者teacher
        :return:
        """
        ret = MyPickle.load(file)
        for i in ret.values():
            if self.name == i.name:
                Public.print("%s已经存在！" % self.name, "error")
                return
        self.num = len(ret) + 1
        self.school = school_obj
        self.classes.clear()
        self.classes[classes_obj.num] = classes_obj
        self.course.clear()
        self.course[course_obj.num] = course_obj
        ret[self.num] = self
        MyPickle.dump(ret, file)
        Public.print("""
                    Create<%s>Success!
                    Name：%s
                    School：%s
                    Classes：%s
                    Course：%s
                """ % (self.name, self.name, school_obj.name, classes_obj.name, course_obj.name))

        ret = MyPickle.load(settings.schoolinfo)
        getattr(ret[school_obj.num], types)[self.num] = self
        MyPickle.dump(ret, settings.schoolinfo)


class Student(Teacher):
    pass
    # def __init__(self, name, num=0, school="", course={}, classes={}):
    #     """
    #     :param name:
    #     :param num:
    #     :param school:
    #     :param course:
    #     :param classes:
    #     """
    #     self.name = name
    #     self.num = num
    #     self.school = school
    #     self.course = course
    #     self.classes = classes
    #
    # def create(self, school_obj, classes_obj, course_obj):
    #     ret = MyPickle.load(settings.studentinfo)
    #     print([ret[i].course for i in ret])
    #     for i in ret.values():
    #         if self.name == i.name:
    #             Public.print("学生已经存在！", "error")
    #             return
    #     self.num = len(ret) + 1
    #     self.school = school_obj
    #     self.classes.clear()
    #     self.classes[classes_obj.num] = classes_obj
    #     self.course.clear()
    #     self.course[course_obj.num] = course_obj
    #     ret[self.num] = self
    #     MyPickle.dump(ret, settings.studentinfo)
    #     Public.print("""
    #                 创建学生<%s>成功!
    #                 学生名称：%s
    #                 所属学校：%s
    #                 所属班级：%s
    #                 所学课程：%s
    #             """ % (self.name, self.name, school_obj.name, classes_obj.name, course_obj.name))
    #
    #     ret = MyPickle.load(settings.schoolinfo)
    #     ret[school_obj.num].student[self.num] = self
    #     MyPickle.dump(ret, settings.schoolinfo)

