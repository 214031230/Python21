import re


url = "/book/add/"

reg = "^/book/$"  # 书籍列表

ret = re.match(reg, url)  # match只从头开始匹配
print(ret)
