import re

"""
re.compile()   --> 将正则表达式编译
re.match()     --> 匹配
re.search()    --> 搜索，只取第一个
re.findall()   --> 找所有的符合要求的
"""

value = "1@qq.com"
value = "ooxx@139.com"
value = "ooxx139.com"

ret = re.match(r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$', value)
print(ret)
