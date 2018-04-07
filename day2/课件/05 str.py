# s = 'python自动化运维21期'
# s1 = s[0]
# print(s1)
# s2 = s[2]
# print(s2)
# s3 = s[-1]
# print(s3)
# s4 = s[-2]
# print(s4)
#切片
# s[起始索引:结束索引+1:步长]
# s1 = s[:6] #顾头不顾腚
# print(s1)
#
# s2 = s[6:9]
# print(s2)
#
# s3 = s[:6:2]
# print(s3)
#
# s4 = s[:]
# print(s4)
#
# s5 = s[-1:-5:-1]  #倒着取值，必须加反向步长
# print(s5)
# s = 'oldBoy'
# * capitalize 首字母大写，其他字母小写
# s1 = s.capitalize()
# print(s1)

# *** 全部大写upper() 全部小写lower()
# s2 = s.upper()
# s3 = s.lower()
# print(s2,s3)

# code = 'QeAr'.upper()
# your_code = input('请输入验证码:').upper()
# if your_code == code:
#     print('验证成功')

#* 大小写反转 swapcase()
# s4 = s.swapcase()
# print(s4)

#*非字母的元素隔开的每个单词首字母大写 title()
# s = 'alex wusir*oldboy3taibia'
# s5 = s.title()  # Alex Wusir*Oldboy3Taibia
# print(s5)

# center 居中，长度自己设定，默认填充物None
# s6 = s.center(30)
# s6 = s.center(30,"*")
# print(s6)
# s = 'oldBoy'
# # *** startswith endswith
# s7 = s.startswith('o')
# s7 = s.startswith('ol')
# s7 = s.startswith('oldBoy')
# s7 = s.startswith('Bo',3,5)
# print(s7)
# s = 'tyoyldBoyrte'
# *** strip 去除首尾的空格，制表符\t,换行符。不仅仅是去除空格....
#lstrip() rstrip()
# print(s)
# s8 = s.strip()
# print(s8)
# s81 = s.strip('t')
# print(s81)
# s81 = s.strip('tey')
# print(s81)

# # 用法1去掉空格
# s = "  oldboy  "
# s8 = s.strip()
# print(s8) # 输出结果为 "oldboy"
#
# # 用法2去掉字母
# s = "oldboy"
#
# s9 = s.strip('o')
# print(s9) # 输出结果为"ldboy"
#
# s10 = s.strip('oy')
# print(s10) # 输出结果为"odb"


# name = input('>>>').strip()
# if name == 'oldboy':
#     print('验证成功')

#*** split  (str ---> list)
# s1 = 'oldboy,wusir,alex'
# s = 'oldboywusiroalex'
# l = s.split()
# print(l)
# l = s1.split(',')
# print(l)
# l2 = s.split('o')  # ['', 'ldb', 'ywusir', 'alex']
# print(l2)
#
# l2 = s.split('o',1)  # ['', 'ldboywusiroalex']
# print(l2)
# s = 'oldBoy'
#join 将list --->str
# s9 = '+'.join(s)
# s9 = '_'.join(s)
# print(s9)
# l1 = ['oldboy','wusir','alex']
# s91 = '_'.join(l1)
# print(s91)


# s = '大铁锤fdsalj铁锤妹妹范德萨'
# #replace
# s10 = s.replace('铁锤','钢蛋')
# print(s10)
# s = "我是好人，你不是好人"
# s1 = s.replace("好人", "坏人")
# s2 = s.replace("好人", "坏人", 1)
# print(s1, s2)

s = 'oldBoy'
#find 通过元素找索引  找不到返回-1
# index 通过元素找索引 找不到报错
# ind = s.find('d')
# print(ind)
# ind = s.find('o')
# print(ind)
# ind = s.find('A')
# print(ind)
# ind = s.index('A')
# print(ind)

#格式化输出format
# res='我叫{}今年{}岁，爱好{}'.format('egon',18,'male')
# print(res)
# res='我叫{0}今年{1}岁，爱好{2},我依然叫{0}'.format('egon',18,'male')
# print(res)
# res='{name} {age} {sex}'.format(sex='male', name='egon', age=18)
# print(res)



# #公共方法：len count
# s = 'fdsafsdagsdafjdskahdhjlsadhfkj'
# print(len(s))
# s = 'fdsadd'
# print(s.count('d'))


name = 'jinxin123'
print(name.isalnum()) #字符串由字母或数字组成
print(name.isalpha()) #字符串只由字母组成
print(name.isdigit()) #字符串只由数字组成
i = '123a'
if i.isdigit():
    i = int(i)
else:
    print("输入有误...")