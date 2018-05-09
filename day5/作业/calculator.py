#!/usr/bin/env python3
import re
# 匹配最小单位的括号
brackets = re.compile("\([^()]+\)")
exp_list = re.compile(r"[\d\.]+|/|-|\+|\*")
# exp_list = re.compile(r"[-?\d\.]+|/|-|\+|\*")


def operation(exp, x):
    """
    实际的运算函数
    :param exp:
    :param x: + - * /
    :return:
    """
    ride_index = exp.index(x)
    if x == "*":
        ret = float(exp[ride_index - 1]) * float(exp[ride_index + 1])
        del exp[ride_index - 1], exp[ride_index - 1], exp[ride_index - 1]
        exp.insert(ride_index - 1, ret)
    elif x == "/":
        ret = float(exp[ride_index - 1]) / float(exp[ride_index + 1])
        del exp[ride_index - 1], exp[ride_index - 1], exp[ride_index - 1]
        exp.insert(ride_index - 1, ret)
    elif x == "+":
        ret = float(exp[ride_index - 1]) + float(exp[ride_index + 1])
        del exp[ride_index - 1], exp[ride_index - 1], exp[ride_index - 1]
        exp.insert(ride_index - 1, ret)
    elif x == "-":
        ret = float(exp[ride_index - 1]) - float(exp[ride_index + 1])
        del exp[ride_index - 1], exp[ride_index - 1], exp[ride_index - 1]
        exp.insert(ride_index - 1, ret)
    return exp


def add_sub(exp):
    """
    此函数只计算加减法
    :param exp: ['1', '-', 6.0, '+', 1.4285714285714286]
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
    :param exp: ['1', '-', '2', '*', '3', '+', '5', '/', '3.5']
                ['1', '-', '6', '+', "1.2", 1 * 4]
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


def basic(exp):
    """
    把表达式转换成列表进行计算
    :param exp:  s = "1- 2 * 3 + 5 / 3.5"
    :return:
    """
    exp = exp.replace(" ", "")  # 去掉表达中的空格
    ret = exp_list.findall(exp)  # 把表达式转换成列表
    md_ret = multiply_divide(ret)  # 获取乘除法结果
    add_s = add_sub(md_ret)  # 获取加减法结果
    return add_s


def calculator(expression):
    """
    判断表达式是否包含括号，如果有括号则进行递归计算，如果没括号直接进行计算
    :param expression:  第一次表达式等于：s = "1- 2 * 3 + 5 / 3.5"
    :return: 计算结果
    """
    if brackets.search(expression) == None:  # 表达式不包含括号的直接开始计算
        ret = basic(expression)  # 交个计算加减乘除的函数进行计算 并返回计算结果
        return ret
    else:  # 表达式包含括号
        ret = brackets.search(expression).group()
        expression = expression.replace(ret, str(basic(ret[1:len(ret) - 1])))  # k[1:len(k) - 1] 把 (-40/5) 切片成 -40/5  -8
        ret = calculator(expression)
        return ret


s = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) ) + ( 4 * 5 )"
# s = "1 - 2 * ( (60-30 +(40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (4*3)/ (16-3*2) ) + ( 4 * 5 )"
if __name__ == "__main__":
    # exp = input("请输入表达式：")
    print("正确答案：", eval(s))
    print(calculator(s))
