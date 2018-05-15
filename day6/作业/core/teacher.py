#!/usr/bin/env python3
class Teacher:
    """教师视图"""
    menus = {"1、查看班级": "",
             "2、查看课程": ""
             }

    def __init__(self, name, classes, course):
        """
        :param name: 老师账号
        :param classes: 班级对象
        :param course: 课程对象
        """
        self.name = name
        self.classes = classes
        self.course = course


class Classes:
    """班级管理"""
    def __init__(self, name, school, course, month, student):
        """
        :param name: 班级名称 例如 python21期
        :param school: 学校对象
        :param course: 课程对象 例如python
        :param month: 课程周期 比如6个月
        :param student: 学生对象
        """
        self.name = name
        self.school = school
        self.course = course
        self.month = month
        self.student = student


class Course:
    """课程管理"""
    def __init__(self, name, month, price):
        """
        :param name: 课程名称
        :param month: 课程周期 例如6个月
        :param price: 课程价格
        """
        self.name = name
        self.month = month
        self.price = price
