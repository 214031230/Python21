#!/usr/bin/env python3
import requests
import time
import hashlib

key = "32425sdf23423tsdf324"
ctime = time.time()

key = "%s|%s" % (key, ctime)
md5 = hashlib.md5()
md5.update(key.encode("utf-8"))
key = md5.hexdigest()

response = requests.post(
    url="http://127.0.0.1:8000/api/test/",
    params={"key": key, "ctime": ctime},
    data={"data": "aaaa"}
)
print(response.text)
# response = requests.get(
#     url="http://127.0.0.1:8000/api/test/",
#     params={"key": key, "ctime": ctime},
# )
# print(response.text)
