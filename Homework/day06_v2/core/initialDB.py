#!/usr/bin/env python3
from conf.config import *
from core.my_pickle import MyPickle


Userinfo = MyPickle(userinfo)
userinfo_load = Userinfo.load()

Classinfo = MyPickle(classinfo)
classinfo_load = Classinfo.load()

Schoolinfo = MyPickle(schoolinfo)
schoolinfo_load = Schoolinfo.load()

Teacherinfo = MyPickle(teacherinfo)
teacherinfo_load = Teacherinfo.load()

Studentinfo = MyPickle(studentinfo)
studentinfo_load = Studentinfo.load()

Courseinfo = MyPickle(courseinfo)
courseinfo_load = Courseinfo.load()
