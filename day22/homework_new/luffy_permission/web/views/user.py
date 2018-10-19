#!/usr/bin/env python3
from django.shortcuts import render, redirect
from rbac import models
from rbac.services import permission


def login(request):
    """
    用户登录页面
        1. Get请求
            1. 返回登录页面
        2. Post请求
            1. 拿到页面通过post传过来的用户名和者密码
            2. 使用orm进行过滤查找
                1. 如果能找到值，则说明登录成功
                    1. 登录成功以后调用rbac函数初始化
                    2. 初始化的主要功能是获取用户的权限和菜单保存到session中
                    3. 跳转到客户列表页面
                2. 登录失败,返回错误信息给页面展示
    :param request: 
    :return: 
    """
    msg = {"msg": ""}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = models.UserInfo.objects.filter(username=username, password=password).first()
        if user_obj:
            permission.init_permission(request, user_obj)
            return redirect("/customer/list/")
        else:
            msg["msg"] = "用户名或者密码错误!"

    return render(request, "login.html", locals())
