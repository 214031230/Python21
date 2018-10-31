import re

string1 = """<div>静夜思
窗前明月光
疑是地上霜
举头望明月
低头思故乡
</div>"""

r=re.findall('.*',string1,re.S)
print(r)