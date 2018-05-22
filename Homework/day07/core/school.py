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
        :return: 
        """
        ret = MyPickle.load(settings.schoolinfo)
        for i in ret.values():
            if self.name == i.name:
                Public.print("学校名已经存在！", "error")
                return
        self.num = len(ret) + 1
        ret[self.num] = self
        MyPickle.dump(ret, settings.schoolinfo)
        Public.print("""
                    创建学校<%s>成功!
                    学校名称：%s
                """ % (self.name, self.name))


class Classes:
    def __init__(self, name, num=0, classes={}):
        """
        :param name: 班级名称
        :param num: 班级id
        :param classes: 班级下有那些学生
        """
        self.name = name
        self.num = num
        self.classes = classes

    def create(self, school):
        """
        创建班级
        :return: 
        """
        ret = MyPickle.load(settings.classinfo)
        for i in ret.values():
            if self.name == i.name:
                Public.print("班级名已经存在！", "error")
                return
        self.num = len(ret) + 1
        ret[self.name] = self
        MyPickle.dump(ret, settings.classinfo)
        Public.print("""
                    创建班级<%s>成功!
                    班级名称：%s
                """ % (self.name, self.name))

        ret = MyPickle.load(settings.schoolinfo)
        ret[school.num].classes[self.name] = self
        MyPickle.dump(ret, settings.schoolinfo)


class Course:
    def __init__(self, name, num=0):
        """
        :param name: 课程名称
        """
        self.name = name
        self.num = num

    def create(self, school):
        """
        创建课程
        :return: 
        """
        ret = MyPickle.load(settings.courseinfo)
        for i in ret.values():
            if self.name == i.name:
                Public.print("课程名已经存在！", "error")
                return
        self.num = len(ret) + 1
        ret[self.name] = self
        MyPickle.dump(ret, settings.courseinfo)
        Public.print("""
                    创建课程<%s>成功!
                    课程名称：%s
                """ % (self.name, self.name))

        ret = MyPickle.load(settings.schoolinfo)
        ret[school.num].course[self.name] = self
        MyPickle.dump(ret, settings.schoolinfo)


class Person:
    def __init__(self, name, age="18", sex="女"):
        self.name = name
        self.age = age
        self.sex = sex

    def login():
        print("\033[0;31;0m")
        print("欢迎访问校园管理系统".center(50, "-"))
        print(">>>请登录：\033[0m")
        count = 0
        while count < 3:
            username = input("\033[0;35;0m>>>请输入用户名：\033[0m").strip()
            password = input("\033[0;35;0m>>>请输入密码：\033[0m").strip()
            if not username or not password:
                print("ERROR:用户名或密码不能为空")
            ret = MyPickle(settings.userinfo)
            user_info = ret.load()
            print(user_info)
            if username in user_info["name"]:
                pwd_index = user_info["name"].index(username)
                if password == user_info["password"][pwd_index]:
                    return username, user_info["type"][pwd_index]
                else:
                    print("ERROR：密码错误")
            else:
                print("ERROR：用户名不存在")
            count += 1


class Teacher(Person):
    def __init__(self, name, age="18", sex="女", school=None, course=None, classes=None):
        super().__init__(name)

    def create(self, school, course):
        create_info_user(settings.teacherinfo, school, course, self)
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
        create_info_user(settings.studentinfo, school, course, self)
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

