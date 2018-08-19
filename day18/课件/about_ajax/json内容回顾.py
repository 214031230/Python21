import json


d1 = {"name": "alex", "age": 9000}
s1 = json.dumps(d1)
print(s1, type(s1))

# 反序列化 字符串 -> Python中的数据类型
d2 = json.loads(s1)
print(d2, type(d2))
