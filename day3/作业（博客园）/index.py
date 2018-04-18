#!/usr/bin/env python3
# dic = {}
# with open("./file/test", encoding="utf-8") as f1:
#     for i in f1:
#         k, v = i.strip().split(":")
#         dic[int(k)] = v
# print(dic)
menu = {1: '请登录',
        2: '请注册',
        3: '文章页面',
        4: '日记页面',
        5: '评论页面',
        6: '收藏页面',
        7: '注销',
        8: '退出程序'}
flag = True
print("欢迎来到博客园首页")
while flag:
    for k, v in menu.items():
        print(k, v)
    choice = input("请选择菜单：")
