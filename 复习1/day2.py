#!/usr/bin/env python3
# l1 = [1, 2, 'alfdsafex', 'wusir',['oldboy', 'ritian', 99], 'taibai']
# l2 = [1, 2, 'alfdsafex', 'wusir',['oldboy', 'ritian', 10], 'taibai']

# 1,将'alex'全部变成大写，放回原处。


# 2，给['oldboy', 'ritian', 99] 追加一个元素‘女神’。 一个方法


# 3，将'ritian'首字母大写，放回原处。


# 4，将99通过数字相加，或者字符串相加或者等等，变成'100'
dic = {
    'name_list': ['b哥', '张帝', '人帅', 'kitty'],
    '老男孩': {
        'name': '老男孩',
        'age': 46,
        'sex': 'ladyboy',
    },
}
# 1,['b哥', '张帝', '人帅', 'kitty']追加一个元素，'骑兵'
dic["name_list"].append("骑兵")
# 2，将kitty全部变成大写。
dic["name_list"][-1] = dic["name_list"][-1].upper()

# 3，将老男孩 改成oldboy。
dic["老男孩"]["name"] = "oldboy"
# 4，将ladyboy首字母大写。
dic["老男孩"]["sex"] = dic["老男孩"]["sex"].capitalize()
print(dic)
