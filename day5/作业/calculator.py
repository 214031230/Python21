#!/usr/bin/env python3
# day5博客地址：http://www.cnblogs.com/spf21/p/9004193.html
import re
# 匹配最小单位的括号内的四则运算
brackets = re.compile("\([^()]+\)")
# 匹配整数、小数、运算符
exp_list = re.compile("[\d\.]+|/|-|\+|\*")
# 匹配非数字、小数、运算符、括号
check_exp = re.compile("[^\d\.\-\+\*/()\s]")


def operation(exp, x):
    """
    实际的四则运算 并判断有没有负数
    :param exp: eq.['1', '*', - , 6.0, '+', 1.4285714285714286]
    :param x: eq. + - * /
    :return:
    """
    ride_index = exp.index(x)
    if exp[ride_index + 1] != '-':  # 判断有没有负数，无负数则正常计算
        global rest
        if x == "*":
            rest = float(exp[ride_index - 1]) * float(exp[ride_index + 1])
        elif x == "/":
            rest = float(exp[ride_index - 1]) / float(exp[ride_index + 1])
        elif x == "+":
            rest = float(exp[ride_index - 1]) + float(exp[ride_index + 1])
        elif x == "-":
            rest = float(exp[ride_index - 1]) - float(exp[ride_index + 1])
        del exp[ride_index - 1], exp[ride_index - 1], exp[ride_index - 1]
        exp.insert(ride_index - 1, rest)
    elif exp[ride_index + 1] == '-':  # 有负数则取索引+2的值
        if x == "*":  # [1,* , -,1]
            rest = -(float(exp[ride_index - 1]) * float(exp[ride_index + 2]))
        elif x == "/":
            rest = -(float(exp[ride_index - 1]) / float(exp[ride_index + 2]))
        elif x == "+":
            rest = float(exp[ride_index - 1]) - float(exp[ride_index + 2])
        elif x == "-":
            rest = float(exp[ride_index - 1]) + float(exp[ride_index + 2])
        del exp[ride_index - 1], exp[ride_index - 1], exp[ride_index - 1], exp[ride_index - 1]
        exp.insert(ride_index - 1, rest)
    return exp


def add_sub(exp):
    """
    此函数只计算加减法
    :param exp: eq.['1', '-', 6.0, '+', 1.4285714285714286]
    :return:
    """
    if "-" in exp and "+" not in exp:
        exp = operation(exp, "-")
    elif "+" in exp and "-" not in exp:
        exp = operation(exp, "+")
    elif "-" in exp and "+" in exp:
        ride_index1 = exp.index("-")
        ride_index2 = exp.index("+")
        if ride_index1 < ride_index2:
            exp = operation(exp, "-")
        else:
            exp = operation(exp, "+")
    else:
        return exp[0]
    return add_sub(exp)


def multiply_divide(exp):
    """
    此函数只计算乘除法
    :param exp: eq.['1', '-', '2', '*', '3', '+', '5', '/', '3.5']
    :return:'
    """
    if "*" in exp and "/" not in exp:
        exp = operation(exp, "*")
    elif "/" in exp and "*" not in exp:
        exp = operation(exp, "/")
    elif "/" in exp and "*" in exp:
        ride_index1 = exp.index("*")
        ride_index2 = exp.index("/")
        if ride_index1 < ride_index2:
            exp = operation(exp, "*")
        else:
            exp = operation(exp, "/")
    else:
        return exp
    return multiply_divide(exp)


def basic(expression):
    """
    把表达式转换成列表进行计算
    :param exp:  s = "1- 2 * 3 + 5 / 3.5"
    :return: 最终的计算结果
    """
    ret_list = expression.replace(" ", "")  # 去掉表达中的空格
    ret = exp_list.findall(ret_list)  # 把表达式转换成列表  [- ,1, -, 2, *, 3 ,+,  5, /, 3.5,]
    if ret[0] == "-":  # 如果第一个元素是-那么第一个数字应该是负数
        ret[0] = ret[0] + ret[1]
        del ret[1]
    return add_sub(multiply_divide(ret))  # 先获取乘除法结果 在获取加减法结果


def calculator(expression):
    """
    判断表达式是否包含括号，如果有括号则进行递归计算，如果没括号直接进行计算
    :param expression:  第一次表达式等于：s = "1- 2 * 3 + 5 / 3.5"
    :return: 最终的计算结果
    """
    if not brackets.search(expression):  # 表达式不包含括号的直接开始计算
        return basic(expression)  # 交给计算加减乘除的函数进行计算 并返回计算结果
    else:  # 表达式包含括号
        ret = brackets.search(expression).group()  # 取一个括号内的四则运算
        expression = expression.replace(ret, str(basic(ret[1:len(ret) - 1])))  # 把的四则运算结果在表达式中替换# k[1:len(k) - 1] 把 (-40/5) 切片成 -40/5  -8
        return calculator(expression)  # 递归处理多个括号的情况，直到没有括号


def helpper():
    """
    帮助文档
    :return:
    """
    with open("./readme", encoding="utf-8") as f1:
        for i in f1:
            print("\033[31;0m%s\033[0m" % i.rstrip())


if __name__ == "__main__":
    helpper()
    while True:
        exp = input("\033[36;0m请输入表达式>>>：\033[0m").strip()
        if not exp:continue
        if exp.lower() == "q":break
        if exp.count("(") != exp.count(")"):
            print("\033[31;0mERROR:语法错误缺少()")
            continue
        if check_exp.search(exp):
            print("\033[31;0mERROR:语法错误未知符号'%s'\033[0m" % check_exp.search(exp).group())
            continue
        print("calculator计算结果：%s" % calculator(exp))
        print("内置eval()计算结果：%s" % eval(exp))

