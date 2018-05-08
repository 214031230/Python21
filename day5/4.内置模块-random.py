#!/usr/bin/env python3
# random 随机数
import random
# random 随机小数
print(random.random())  # 0 - 1之间随机小数
# uniform 随机范围小数
print(random.uniform(1, 4))  # 1 - 4 之间随机小数

# 随机整数
# randint 随机范围内整数
print(random.randint(1, 10))
# randrange 随机范围内的奇数
print(random.randrange(1, 10, 2))

# choice 随机一个返回值
print(random.choice([1, 2, 3, 4, 5]))
# sample 随机多个返回值
print(random.sample([1, 2, 3, 4, 5], 2))

# shuffle 打乱顺序
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print(lst)


#  练习：生成随机验证码
# s = ""
# for i in range(2):
#     s += "".join(random.sample([chr(random.randint(65, 90)), chr(random.randint(97, 122)), str(random.randint(0, 9))], 3))
# print(s)

def func(num):
    """
    随机验证码包含大小写字母数字
    :param num: 验证码位数
    :return:
    """
    code = ""
    for i in range(num):
        digit = str(random.randint(0, 9))
        letter = chr(random.randint(65, 90))
        capital = chr(random.randint(97, 122))
        rdom = random.choice([digit, letter, capital])
        code += rdom
    return code
print(func(6))