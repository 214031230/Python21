#!/usr/bin/env python3
import re
# # findall 返回所有满足匹配条件的结果,放在列表里
# s = "1+2+(1*(1+2))+2+(1*4)"
# s1 = "1+2+1+(1*3)+2+(1*4)"
# print(re.findall("\(.+?\)\)?", s))
#
# # search 函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。
# print(re.search("\d", s))
# print(re.search("\d", s).group())
#
# # match 同search,不过在字符串开始处进行匹配
# print(re.match("\W", s))
# print(re.match("\d", s).group())
#
# # split   # 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
# print(re.split('[ab]', 'abcd'))
#
# # sub 替换 默认替换所有
# print(re.sub("\d", "H", s))
# # 指定替换次数
# print(re.sub("\d", "H", s, 1))
#
# # subn 将数字替换成'H'，返回元组(替换的结果,替换了多少次)
# print(re.subn("\d", "H", s))
#
#
# # compile  将正则表达式编译成为一个 正则表达式对象，规则要匹配的是3个数字
# obj = re.compile("\d{3}")
# print(obj.findall("aaa123aaa456"))  # 正则表达式对象调用search，参数为待匹配的字符串
#
# # finditer
# res = re.finditer("\d", s1)
# print(next(res).group())
# print(next(res).group())
#
# # findall 优先级别
# ret = re.findall('www.(baidu|oldboy).com', 'www.oldboy.com')
# print(ret)
# print(re.findall('www.(?:baidu|oldboy).com', 'www.oldboy.com'))
#
# # split 优先级别
# ret = re.split("\d+", "eva3egon4yuan")
# print(ret)
# ret = re.split("(\d+)", "eva3egon4yuan")
# print(ret)

# re模块综合练习题
# 1、匹配整数
s = "1-2*(60+(-40.35/5)-(-4*3))"
print(re.findall("-?\d+\.?\d*", s))

s = "afasfas12323@qq.com asdfsd@sasdf@aslan@sdlfjsfd"
print(re.findall("\d+@[a-z]{1,3}\.[a-z]{1,3}", s))