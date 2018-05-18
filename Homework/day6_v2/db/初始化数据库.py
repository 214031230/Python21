#!/usr/bin/env python3
from core.my_pickle import MyPickle
from conf import config
userinfo = {"name": ["admin"], "password": ["123"], "type": ["Manager"]}
schoolinfo = {}
teacherinfo = {}
studentinfo = {}
classinfo = {}
courseinfo = {}

f1 = MyPickle(config.userinfo)
f1.dump(userinfo)
f1 = MyPickle(config.schoolinfo)
f1.dump(schoolinfo)
f1 = MyPickle(config.teacherinfo)
f1.dump(teacherinfo)
f1 = MyPickle(config.studentinfo)
f1.dump(studentinfo)
f1 = MyPickle(config.classinfo)
f1.dump(classinfo)
f1 = MyPickle(config.courseinfo)
f1.dump(courseinfo)