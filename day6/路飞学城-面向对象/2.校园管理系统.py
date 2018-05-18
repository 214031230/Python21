#!/usr/bin/env python3
class School:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def create(self):
        print("创建学校<%s>成功!" % self.name)


class Classes:
    def __init__(self, name):
        self.name = name

    def create(self):
        print("创建班级<%s>成功!" % self.name)


class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Teacher(Person):
    def __init__(self, name, age, sex, level, wages, courses={}, classes={}):
        super().__init__(name, age, sex)
        self.level = level
        self.wages = wages
        self.courses = courses
        self.classes = classes

    def create(self, school):
        print("%s学校创建老师<%s>成功!" % (school.name, self.name))

    def brond_classes(self, classes):
        self.classes[classes.name] = classes
        print("<%s>老师负责<%s>班级" % (self.name, classes.name))

    def brond_course(self, course):
        self.courses[course.name] = course
        print("<%s>老师选择了<%s>课程" % (self.name, course.name))


class Student(Person):
    def __init__(self, name, age, sex, class_time):
        super().__init__(name, age, sex)
        self.class_time = class_time

    def create(self, school):
        print("%s学校创建学生<%s>成功!" % (school.name, self.name))

    def brond_classes(self,classes):
        print("<%s>学生被分配到<%s>班级" % (self.name, classes.name))

    def brond_course(self, course):
        print("<%s>学生选择了<%s>课程" % (self.name, course.name))


class Course:
    def __init__(self, name, moth, price):
        self.name = name
        self.moth = moth
        self.price = price

    def create(self, school):
        print("<%s>创建课程<%s>成功!" % (school.name, self.name))


# 北京老男孩
    # linux python
# 上海老男孩
    # go

bjoldboy = School("北京老男孩", "北京昌平沙河")
sholdboy = School("上海老男孩", "北京昌平沙河")
alex = Teacher("alex", 18, "男", 1, 5000)
egon = Teacher("egon", 18, "男", 1, 5000)
spf = Student("孙鹏飞", 18, "男", "9:00")
python = Course("Python", 6, 10000)
linux = Course("Linux", 4, 5000)
go = Course("Go", 4, 5000)

# 老师绑定学校
alex.school = bjoldboy
egon.school = sholdboy


# 学校绑定课程
bjoldboy.course = {}
bjoldboy.course[linux.name] = linux
bjoldboy.course[python.name] = python

sholdboy.course = {}
sholdboy.course[go.name] = go

import pickle
# 老师选择课程
for index, k in enumerate(alex.school.course, 1):
    print("%s.%s" % (index, k))
while True:
    choice = input(">>>请选择课程：")
    alex.brond_course(alex.school.course[choice])
    for i in alex.courses:
        print(i)

    teacher_info = {}
    teacher_info[alex.name] = alex
    ret = pickle.dumps(teacher_info)
    print(pickle.loads(ret)[alex.name].name)
    # ret = pickle.dumps(alex)
    # print(teacher_info[alex.name].name)
    # ret1 = pickle.loads(ret[alex.name])
    # ret1 = pickle.loads(ret)

    # print(ret1)
# print(alex.school.course[python.name].name)
# print(alex.school.course[linux.name].name)
#
# print(egon.school.course[go.name].name)

