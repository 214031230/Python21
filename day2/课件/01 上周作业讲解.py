'''
1、使用while循环输入 1 2 3 4 5 6     8 9 10

2、求1-100的所有数的和

3、输出 1-100 内的所有奇数

4、输出 1-100 内的所有偶数

5、求1-2+3-4+5 ... 99的所有数的和

6、用户登陆（三次机会重试）
'''
#1、使用while循环输入 1 2 3 4 5 6 8 9 10
# count = 1
# while count < 11:
#     if count == 7:
#         count += 1
#     print(count)
#     count += 1

#3、输出 1-100 内的所有奇数
# count = 1
# while count < 101:
#     print(count)
#     count += 2

#5、求1-2+3-4+5 ... 99的所有数的和
# sum = 0
# count = 1
# while count < 100:
#     if count % 2 == 0:
#         sum -= count
#     else:
#         sum += count
#     count += 1
# print(sum)
'''
li = [{'username':'alex','password':'SB'},
    {'username':'wusir','password':'sb'},
    {'username':'taibai','password':'男神'},
      ]
#客户输入了三次机会，都没成功，给它一个选择，让它在试试
# Y 再给他三次机会...不输入了，print('臭不要脸.....')
'''
li = [{'username':'alex','password':'SB'},
    {'username':'wusir','password':'sb'},
    {'username':'taibai','password':'男神'},
      ]
j = 0
while j < 3:
    username = input('姓名：')
    password = input('密码：')
    for i in li:
        if username == i['username'] and password == i['password']:
            print('登录成功')
            j = 3
            break
    else:
        print('登录不成功，请重新输入')
        if j == 2:
            choice = input('是否在试试？Y')
            if choice == 'Y':
                j = -1
    j += 1

