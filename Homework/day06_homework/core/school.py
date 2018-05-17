#!/usr/bin/env python3
class School:
    def __init__(self, sid, name, city):
        """
        :param name: 学校名称
        :param city: 学校所在城市
        """
        self.sid = sid
        self.name = name
        self.city = city


class Teacher:
    def __init__(self, name, school_name, classes, course):
        """
        :param name: 老师账号
        :param school: 学校对象
        :param classes: 班级对象
        :param course: 课程对象
        """
        self.name = name
        self.school_name = school_name
        self.classes = classes
        self.course = course


class Student:
    def __init__(self, name, school, classes, course):
        """
        :param name: 学员账号
        :param school: 学校对象
        :param classes: 班级对象
        :param course: 课程对象
        """
        self.name = name
        self.school = school
        self.classes = classes
        self.course = course


class Classes:
    def __init__(self, name, school, course=None, student=None):
        """
        :param name: 班级名称 例如 python21期
        :param school: 学校对象
        :param course: 课程对象 例如python
        :param student: 学生对象
        """
        self.name = name
        self.school = school
        self.course = course
        self.student = student


class Course:
    """课程管理"""
    def __init__(self, name, school, month=None, price=None):
        """
        :param name: 课程名称
        :param school: 课程开设学校
        :param month: 课程周期 例如6个月
        :param price: 课程价格
        """
        self.name = name
        self.school = school
        self.month = month
        self.price = price
