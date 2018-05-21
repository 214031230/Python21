#!/usr/bin/env python3
from core import my_pickle
from conf import config
userinfo = {"name": ["admin"], "password": ["123"], "type": ["Manager"]}
schoolinfo = {}
teacherinfo = {}
studentinfo = {}
classinfo = {}
courseinfo = {}

my_pickle.dump(userinfo, config.userinfo)
my_pickle.dump(schoolinfo, config.schoolinfo)
my_pickle.dump(teacherinfo, config.teacherinfo)
my_pickle.dump(studentinfo, config.studentinfo)
my_pickle.dump(courseinfo, config.courseinfo)
my_pickle.dump(classinfo, config.classinfo)