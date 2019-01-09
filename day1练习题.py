# 1.简述变量命名规范
print("""
变量命名规范:
    1.由数字,字母或下划线组成
    2.不能是数字开头,也不能全是数字
    3.不能是python的关键字
    4.不能用中文
    5.要有意义
    6.使用驼峰或者下划线命名,驼峰要首字母大写,下划线是要每个单词使用_分开
    7.不要太长
	8.要区分大小写
    
""")

# 2.name = input(">>>") name变量是什么数据类型
# name = input(">>>")
# print(type(name))
print('name = input(">>>") name变量是str类型')

# 3.if条件语句的基本结构?
print("""
if条件语句的基本结构:
1.
if 条件判断:
	if-语句块
	
2.
if 条件判断:
	if-语句块
else:
	else-语句块
	
3.
if 条件判断:
	if-语句块
elif 条件判断2:
	elif1-语句块
elif 条件判断3:
	elif2-语句块
elif 条件判断4:
	elif3-语句块
...
else:
	else-语句块

4.
if语句可以相互嵌套,可以无限嵌套,一般写程序不要超过5层
    
""")

# 4.用print打印出下面内容 
#   文能提笔安天下,
#	武能上马定乾坤.
#	心存谋略何人胜,
#	古今英雄唯是君.
print("""
    文能提笔安天下,
    武能上马定乾坤.
    心存谋略何人胜,
    古今英雄唯是君.
""")
# 5.利用if语句写出猜大小游戏
# 设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确。
print("猜大小游戏")
# GuessNumber = int(input("请输入要猜测的数字:"))
GuessNumber = 66
while True:
    YourNumber = input("请输入你猜想的数字:")
    # 判断输入的是否是数字,否则提示错误信息
    InputType = YourNumber.isdigit()
    if InputType == True:
        if int(YourNumber) > GuessNumber:
            print("猜测的结果大了")
        elif int(YourNumber) < GuessNumber:
            print("猜测的结果小了")
        else:
            print("结果正确")
            break
    else:
        print("请输入数字!")

# 6、提示用户输入他的年龄, 程序进判断.
# 如果小于10, 提示小屁孩,
# 如果大于10, 小于于 20, 提示青春期叛逆的小屁孩.
# 如果大于20, 小于30. 提示开始定性, 开始混社会的小屁孩儿,
# 如果大于30, 小于40. 体制看老大不小了, 赶紧结婚小屁孩儿.
# 如果大于40, 小于50. 提示家里有个不听话的小屁孩儿.
# 如果大于50, 小于60. 提示自己马上变成不听话的老屁孩儿.
# 如果大于60, 小于70. 提示活着还不错的老屁孩儿.
# 如果大于70, 小于于 90. 提示人生就快结束了的一个老屁孩儿.
# 如果大于90以上. 提示. 再见了这个世界.
while True:
    age = input("请输入您的年龄(输入Q退出):")
    if age == "Q":
        break
    # 用户输入除Q以外的非数字提示错误
    AgeType = age.isdigit()
    if InputType == True:
        if int(age) < 10:
            print("小屁孩.")
        elif int(age) <= 20:
            print("青春期叛逆的小屁孩.")
        elif int(age) < 30:
            print("开始定性, 开始混社会的小屁孩儿.")
        elif int(age) < 40:
            print("看老大不小了, 赶紧结婚小屁孩儿.")
        elif int(age) < 50:
            print("家里有个不听话的小屁孩儿.")
        elif int(age) < 60:
            print("自己马上变成不听话的老屁孩儿.")
        elif int(age) < 70:
            print("活着还不错的老屁孩儿.")
        elif int(age) <= 90:
            print("人生就快结束了的一个老屁孩儿.")
        else:
            print("再见了这个世界.")
    else:
        print("请输入数字!")

# 7、单行注释以及多行注释？
print('''
	使用#号来进行单行注释,
	多行注释也就是块注释:用三个单引号或者三个双引号进行注释.
''')

# 8、简述你所知道的Python3x和Python2x的区别？
print('''
Python2x 源码重复,不规范;默认是ASCII编码;即将被淘汰
Python3x 整合源码,更清晰优美;默认是utf-8;重新架构的
''')

# 9、提示用户输入麻花藤. 判断用户输入的对不对. 如果对, 提示真聪明, 如果不对, 提示你是傻逼么
qqBossName = input("请输入麻花藤:")
if qqBossName == "麻花藤":
    print("真聪明.")
else:
    print("你是傻逼么.")

# 10、使用while循环输入 1 2 3 4 5 6     8 9 10
count = 1
while count <= 10:
    if count == 7:
        count = count + 1
        continue
    else:
        print(count)
    count = count + 1

# 11、求1-100的所有数的和
# 定义接收1-100的所有数的和
sum100 = 0
# 定义循环次数
numIndex = 1
while numIndex <= 100:
    sum100 = sum100 + numIndex
    numIndex = numIndex + 1
print(sum100)
# 12、输出 1-100 内的所有奇数
# 定义循环次数
oddIndex = 1
while oddIndex <= 100:
    oddNumber = oddIndex % 2
    if int(oddNumber) != 0:
        print(oddIndex)
    oddIndex = oddIndex + 1

# 13、输出 1-100 内的所有偶数
# 定义循环次数
evenIndex = 1
while evenIndex <= 100:
    evenNumber = evenIndex % 2
    if int(evenNumber) == 0:
        print(evenIndex)
    evenIndex = evenIndex + 1

# 14、求1-2+3-4+5 ... 99的所有数的和
# 定义接收奇数和
oddSum = 0
# 定义接收偶数和
evenSum = 0
# 定义循环次数
index = 1
while index < 100:
    if int(index % 2) == 0:
        evenSum = evenSum + index
    else:
        oddSum = oddSum + index
    index = index + 1
print(oddSum - evenSum)


str