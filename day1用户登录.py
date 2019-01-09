
print("欢迎登陆王志宾系统")
# 定义正确的用户名
userName = "wangzhibin"
# 定义正确的登录密码
passWord = "123456"
# 定义输入次数
inputCount = 1
# 循环输入次数
while inputCount <= 3:
    # 定义输入的用户名
    inputUserName = input("请输入用户名:")
    # 定义输入的登录密码
    inputPassWord = input("请输入登录密码:")
   
    if inputUserName == userName and inputPassWord == passWord:
        print("登录成功!")
        break
    else:
        # 定义剩余输入次数
        remainCount = 3 - inputCount
        if remainCount == 0:
            print("用户名或密码错误,超出输入次数,您被限制登录!")
        else:
            print("用户名或密码错误,请重新登录!(您还有" + str(remainCount) + "次输入机会)")
        inputCount = inputCount + 1


str