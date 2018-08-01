#!/usr/bin/env python3
# import json
# import pickle
#
# dic = {"name": "sunpengfei"}
# ret = json.dumps(dic)
# print(ret)
# ret = json.loads(ret)
# print(ret)
#
# ret = pickle.dumps(dic)
# print(ret)
# ret = pickle.loads(ret)
# print(ret)
# import hashlib
# md5 = hashlib.md5()
# md5.update("123".encode("utf-8"))
# print(md5.hexdigest())
#
# md5 = hashlib.md5("123".encode("utf-8"))
# md5.update("123".encode("utf-8"))
# print(md5.hexdigest())

# import hashlib
# with open("day8.py", "rb") as f1:
#     md5 = hashlib.md5()
#     for i in f1:
#         md5.update(i)
#     print(md5.hexdigest())
# with open("day9.py", "rb") as f1:
#     md5 = hashlib.md5()
#     for i in f1:
#         md5.update(i)
#     print(md5.hexdigest())


# import configparser
# conf = configparser.ConfigParser()
# conf.read("hosts.ini")
# print(conf.sections())