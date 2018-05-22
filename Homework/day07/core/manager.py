#!/usr/bin/env python3
from core.school import *
from conf import settings
from core.public import *


class Manager:
    menus = [["1.创建学校 ", "create_school"],
             ["2.查看学校 ", "show_school"],
             ["3.创建班级 ", "create_classes"],
             ["4.查看班级 ", "show_classes"],
             ["5.创建课程 ", "create_course"],
             ["6.查看课程 ", "show_course"],
             ["7.创建讲师 ", "create_teacher"],
             ["8.查看讲师 ", "show_teacher"],
             ["9.创建学员 ", "create_student"],
             ["10.查看学员 ", "show_student"],
             ["11.初始化数据库 ", "initdb"],
             ["Q/q.退出 ", "sys_exit"]
             ]

    def __init__(self, name):
        """
        :param name: 管理账号
        """
        self.name = name
        self.log = Public.log()

    def create_school(self):
        """创建学校"""
        name = input(">>>请输入学校名称：")
        obj = School(name)
        obj.create()
        self.log.info("%s创建了<%s>学校" % (self.name, name))

    def show_school(self):
        """查看学校"""
        ret = Public.check_show(settings.schoolinfo, "学校")
        if ret:
            Public.print("学校列表：", "none")
            for i in ret.values():
                Public.print("        %s.%s" % (i.num, i.name), "none")

    def create_classes(self):
        """创建班级"""
        name = input(">>>请输入班级名称：")
        self.show_school()
        while True:
            school_num = input(">>>请选择学校(输入学校ID)：")
            try:
                ret = MyPickle.load(settings.schoolinfo)
                obj = Classes(name)
                obj.create(ret[school_num])
                break
            except KeyError:
                print_log("请输入正确的学校名称", "error")

    def show_classes(self):
        """查看班级"""
        ret = check_show(settings.classinfo, "班级")
        if ret:
            for i in ret.values():
                print_log("""
                         学校名称：%s""" % i.name, None)
                for k in i.classes.values():
                    print_log("""
                                班级名称：%s""" % k.name, None)

    def create_course(self):
        """创建课程"""
        name = input(">>>请输课程名称：")
        month = input(">>>请输入课程周期：")
        price = input(">>>请输入课程价格：")
        self.show_school()
        while True:
            school_name = input(">>>请选择学校名称：")
            try:
                ret = mypickle.load(settings.schoolinfo)
                obj = Course(name, month, price)
                obj.create(ret[school_name])
                break
            except KeyError:
                print_log("请输入正确的学校名称", "error")

    def show_course(self, name=None):
        """查看课程"""
        if name:
            for i in name:
                print_log("""
                        课程名称：%s""" % i, None)
                return
        ret = check_show(settings.courseinfo, "课程")
        if ret:
            for i in ret.values():
                print_log("""
                         学校名称：%s""" % i.name, None)
                for k in i.course.values():
                    print_log("""
                                课程名称：%s  课程价格：%s  课程周期：%s """ % (k.name, k.price, k.moth), None)
            
    def create_teacher(self):
        """创建老师"""
        name = input(">>>请输入老师账号：")
        self.show_school()
        school = input(">>>请绑定学校：")
        ret = mypickle.load(settings.courseinfo)
        self.show_course(ret[school].course)
        course = input(">>>请绑定的课程：")
        obj = Teacher(name)
        obj.create(ret[school], ret[school].course[course])

    def show_teacher(self):
        """查看老师"""
        ret = check_show(settings.teacherinfo, "老师")
        for k, v in ret.items():
            print_log("""
                        老师名称：%s  所属学校：%s  专业技能：%s""" % (k, v.name, v.course.name), None)

    def create_student(self):
        """创建学生"""
        name = input(">>>请输入学生账号：")
        self.show_school()
        school = input(">>>请选择学校：")
        ret = mypickle.load(settings.courseinfo)
        self.show_course(ret[school].course)
        course = input(">>>请选择课程：")
        obj = Student(name)
        obj.create(ret[school], ret[school].course[course])

    def show_student(self):
        """查看学生"""
        ret = check_show(settings.studentinfo, "学生")
        for k, v in ret.items():
            print_log("""
                        学生名称：%s  所属学校：%s  课程：%s""" % (k, v.name, v.course.name), None)

    def sys_exit(self):
        exit()

    def initdb(self):
        userinfo = {"name": ["admin"], "password": ["0192023a7bbd73250516f069df18b500"], "type": ["Manager"]}
        schoolinfo = {}
        teacherinfo = {}
        studentinfo = {}
        classinfo = {}
        courseinfo = {}
        MyPickle.dump(userinfo, settings.userinfo)
        MyPickle.dump(schoolinfo, settings.schoolinfo)
        MyPickle.dump(teacherinfo, settings.teacherinfo)
        MyPickle.dump(studentinfo, settings.studentinfo)
        MyPickle.dump(courseinfo, settings.courseinfo)
        MyPickle.dump(classinfo, settings.classinfo)




