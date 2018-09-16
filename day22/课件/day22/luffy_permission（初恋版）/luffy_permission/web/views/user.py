"""
跟用户相关的视图都写在这里
"""

from django.shortcuts import render, redirect, HttpResponse
from rbac.models import UserInfo
from rbac.serives.permission import init_permission


def login(request):
    error_msg = ""
    if request.method == "POST":
        # 取数据
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        # 校验
        user_obj = UserInfo.objects.filter(username=username, password=pwd).first()
        if user_obj:
            # 登陆成功
            # 调用封装好的初始化函数
            init_permission(request, user_obj)
            # 后续访问其他页面的时候，要判断访问的url在不在权限列表里
            return redirect("/customer/list/")
        else:
            # 登录失败
            error_msg = "用户名或密码错误"

    return render(request, "login.html", {"error_msg": error_msg})
