#!/usr/bin/env python3
import pickle


class School:
    def __init__(self, name):
        self.name = name

    def create(self):
        return self.name


class Classes:
    def __init__(self, name, school_name):
        self.name = name
        self.school_name = School(school_name)

    def create(self):
        return self.school_name.name, self.name
# info = {}
# c_obj = Classes("一班", "清华大学")
# f = open("test.pkl", mode="wb")
# pickle.dump({1: c_obj}, f)
# f.close()

f = open("test.pkl", mode="rb")
ret = pickle.load(f)
f.close()
print(ret[1].name)
print(ret[1].school_name.name)
print(ret[1].create())