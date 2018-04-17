#!/usr/bin/env python3
# 2、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
li = [1, 2, 3, 4, 5, 6, 7]
t1 = (1, 2, 3, 4, 5, 6, 7)
# print(li[1::2])
# print(t1[1::2])


def fun1(argv):
    return argv[0::2]


print(fun1(li))

# 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。


def fun2(argv):
    if len(argv) > 5:
        return True
    else:
        return False


print(fun2(li))
# 4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。


def fun3(argv):
    if len(argv) > 2:
        return argv[0:2]


print(fun3(li))
# 5、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数，并返回结果。
s1 = "afs234ljL   dfljdfs   LJJ#$ LJDFl"


def fun4(argv):
    isdigit = 0
    isalpha = 0
    isspace = 0
    other = 0
    for i in argv:
        if i.isdigit():
            isdigit += 1
        elif i.isalpha():
            isalpha += 1
        elif i.isspace():
            isspace += 1
        else:
            other += 1
    return "数字个数:%s\n字母个数:%s\n空格个数:%s\n其他个数:%s" % (isdigit, isalpha, isspace, other)


print(fun4(s1))

# 6、写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容，并返回结果。

# s1 = "dafsdf"


def fun5(argv):
    for i in argv:
        if i.isspace():
            return "包含空格"


print(fun5(s1))
# 7、写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# 	dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# 	PS:字典中的value只能是字符串或列表
dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}


def fun6(argv):
    for k, v in argv.items():
        # print(k, v)
        if len(v) > 2:
            argv[k] = v[0:2]
    return argv


print(fun6(dic))
# 8、写函数，接收两个数字参数，返回比较大的那个数字。


def fun7(argv1, argv2):
    if argv1 > argv2:
        return argv1
    else:
        return argv2


print(fun7(5, 1))
# 9、写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（进阶）。


# 10、写一个函数完成三次登陆功能，再写一个函数完成注册功能(进阶)

