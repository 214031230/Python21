#!/usr/bin/env python3
from core.school import *
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
             ["11.初始化数据库 ", "init_db"],
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
        while 1:
            name = input(">>>请输入学校名称(B/b返回)：").strip()
            if not name:continue
            if name.upper() == "B":break
            obj = School(name)
            ret = obj.create()
            if ret == 0:continue
            if ret == 1:
                self.log.info("%s创建了<%s>学校" % (self.name, name))
                break

    def create_classes(self):
        """创建班级"""
        Public.m_create_info(self, Classes, settings.classinfo, "classes")

    def create_course(self):
        """创建课程"""
        Public.m_create_info(self, Course, settings.courseinfo, "course")

    def create_teacher(self):
        """创建老师"""
        Public.m_create_info(self, Teacher, settings.teacherinfo, "teacher", "TeacherManager")

    def create_student(self):
        """创建学生"""
        Public.m_create_info(self, Student, settings.studentinfo, "student", "StudentManager")

    def show_school(self):
        """
        查看学校
        :return: 1 = 找到学校返回1
        """
        ret = Public.check_show(settings.schoolinfo, "学校")
        if ret:
            Public.print("学校列表：", "none")
            for i in ret.values():
                Public.print("        %s.%s" % (i.num, i.name), "none")
            self.log.info("%s查看了学校信息" % self.name)
            return 1

    def show_classes(self, school_num=0):
        """查看班级"""
        Public.m_show_course_class(school_num, "classes", "班级")
        self.log.info("%s查看了学生" % self.name)

    def show_course(self, school_num=0):
        """查看课程"""
        Public.m_show_course_class(school_num, "course", "课程")
        self.log.info("%s查看了课程" % self.name)

    def show_teacher(self, teacher_name="", types=""):
        """查看老师"""
        Public.m_show_teacher_student(teacher_name, types, "老师", settings.teacherinfo)
        self.log.info("%s查看了老师" % self.name)

    def show_student(self, student_name="", types=""):
        """查看学生"""
        Public.m_show_teacher_student(student_name, types, "学生", settings.studentinfo)
        self.log.info("%s查看了学生" % self.name)

    def sys_exit(self):
        """程序退出"""
        self.log.info("%s 退出了程序" % self.name)
        exit()

    def init_db(self):
        """初始化数据库"""
        while True:
            choice = input(">>>Y/N：").strip()
            if choice.upper() == "Y":
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
                Public.print("初始化成功")
                self.log.info("%s 执行了数据库初始化" % self.name)
                break
            elif choice.upper() == "N":
                break
            else:
                Public.print("请输入正确Y/N！", "error")




