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
            if ret == 1:self.log.info("%s创建了<%s>学校" % (self.name, name))

    def create_classes(self):
        """创建班级"""
        name = input(">>>请输入班级名称：")
        self.show_school()
        ret = Public.m_create_course_class(name, Classes, settings.classinfo, "classes")
        if ret == 1:self.log.info("%s创建了班级:%s" % (self.name, name))
        # while True:
        #     school_num = int(input(">>>请选择学校(输入学校ID)：").strip())
        #     try:
        #         ret = MyPickle.load(settings.schoolinfo)
        #         obj = Classes(name)
        #         obj.create(ret[school_num])
        #         break
        #     except KeyError:
        #         Public.print("请输入正确的学校ID", "error")

    def create_course(self):
        """创建课程"""
        name = input(">>>请输入课程名称：")
        self.show_school()
        ret = Public.m_create_course_class(name, Course, settings.courseinfo, "course")
        if ret == 1: self.log.info("%s创建了课程:%s" % (self.name, name))
        # while True:
        #     school_num = int(input(">>>请选择学校(输入学校ID)："))
        #     try:
        #         ret = MyPickle.load(settings.schoolinfo)
        #         obj = Course(name)
        #         obj.create(ret[school_num])
        #         break
        #     except KeyError:
        #         Public.print("请输入正确的学校ID", "error")

    def create_teacher(self):
        """创建老师"""
        name = input(">>>请输入老师名称：")
        self.show_school()
        school_num = int(input(">>>请选择学校(输入学校ID)：").strip())
        self.show_classes(school_num)
        classes_num = int(input(">>>请选择班级(输入班级ID)：").strip())
        self.show_course(school_num)
        course_num = int(input(">>>请选择课程(输入课程ID)：").strip())
        Public.m_create_student_teacher(name, "TeacherManager", Teacher, school_num, classes_num, course_num, settings.teacherinfo, "teacher")
        # school_ret = MyPickle.load(settings.schoolinfo)
        # classes_ret = MyPickle.load(settings.classinfo)
        # course_ret = MyPickle.load(settings.courseinfo)
        # obj = Teacher(name)
        # obj.create(school_ret[school_num], classes_ret[classes_num], course_ret[course_num])
        # MyLogin.register(name, "TeacherManager")

    def create_student(self):
        """创建学生"""
        name = input(">>>请输入学生名称：")
        self.show_school()
        school_num = int(input(">>>请选择学校(输入学校ID)：").strip())
        self.show_classes(school_num)
        classes_num = int(input(">>>请选择班级(输入班级ID)：").strip())
        self.show_course(school_num)
        course_num = int(input(">>>请选择课程(输入课程ID)：").strip())
        Public.m_create_student_teacher(name, "StudentManager", Student, school_num, classes_num, course_num, settings.studentinfo, "student")
        # school_ret = MyPickle.load(settings.schoolinfo)
        # classes_ret = MyPickle.load(settings.classinfo)
        # course_ret = MyPickle.load(settings.courseinfo)
        # obj = Student(name)
        # obj.create(school_ret[school_num], classes_ret[classes_num], course_ret[course_num])
        # MyLogin.register(name, "StudentManager")

    def show_school(self):
        """查看学校"""
        ret = Public.check_show(settings.schoolinfo, "学校")
        if ret:
            Public.print("学校列表：", "none")
            for i in ret.values():
                Public.print("        %s.%s" % (i.num, i.name), "none")
        self.log.info("%s查看了学校" % self.name)

    def show_classes(self, school_num=0):
        """查看班级"""
        Public.m_show_course_class(school_num, "classes", "班级")
        # ret = Public.check_show(settings.schoolinfo, "班级")
        # if not school_num:
        #     for i in ret.values():
        #         Public.print("学校名称：%s" % i .name, "none")
        #         Public.print("班级列表：", "none")
        #         for x in i.classes.values():
        #             Public.print("%s.%s" % (x.num, x.name), "none")
        # else:
        #     Public.print("学校名称：%s" % ret[school_num].name, "none")
        #     Public.print("班级列表：", "none")
        #     for i in ret[school_num].classes.values():
        #         Public.print("%s.%s" % (i.num, i.name), "none")

    def show_course(self, school_num=0):
        """查看课程"""
        Public.m_show_course_class(school_num, "course", "课程")
        # ret = Public.check_show(settings.schoolinfo, "课程")
        # if not school_num:
        #     for i in ret.values():
        #         Public.print("学校名称：%s" % i .name, "none")
        #         Public.print("课程列表：", "none")
        #         for x in i.course.values():
        #             Public.print("%s.%s" % (x.num, x.name), "none")
        # else:
        #     Public.print("学校名称：%s" % ret[school_num].name, "none")
        #     Public.print("课程列表：", "none")
        #     for i in ret[school_num].course.values():
        #         Public.print("%s.%s" % (i.num, i.name), "none")

    def show_teacher(self, teacher_name="", types=""):
        """查看老师"""
        Public.m_show_teacher_student(teacher_name, types, "老师", settings.teacherinfo)
        # ret = Public.check_show(settings.teacherinfo, "老师")
        # for i in ret.values():
        #     if not teacher_name:
        #         Public.print("%s.老师名称：<%s> 所属学校：<%s> 所交课程：<%s> 所教班级:<%s>"
        #                     % (i.num, i.name, i.school.name, [i.course[x].name for x in i.course], [i.classes[x].name for x in i.classes]))
        #     else:
        #         if teacher_name == i.name:
        #             Public.print("%s: <%s>"
        #                          % (types, [getattr(i, types)[x].name for x in getattr(i, types)]))

    def show_student(self, student_name="", types=""):
        """查看学生"""
        Public.m_show_teacher_student(student_name, types, "学生", settings.studentinfo)
        # ret = Public.check_show(settings.studentinfo, "学生")
        # for i in ret.values():
        #     if not student_name:
        #         Public.print("%s.学生名称：<%s> 所属学校：<%s> 所学课程：<%s> 所所班级:<%s>"
        #                         % (i.num, i.name, i.school.name, [i.course[x].name for x in i.course], [i.classes[x].name for x in i.classes]))
        #     else:
        #         if student_name == i.name:
        #             Public.print("%s: <%s>"
        #                          % (types, [getattr(i, types)[x].name for x in getattr(i, types)]))

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




