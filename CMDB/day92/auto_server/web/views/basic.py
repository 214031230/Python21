#!/usr/bin/env python3
from django.shortcuts import render, redirect
from repository import models
from django.urls import reverse
from rbac.service.permission import init_permission


def index(request):
    """
    欢迎页面
    :param request:
    :return:
    """
    return render(request, "web/index.html")


def login(request):
    """
    用户登录
    :param request:
    :return:
    """
    if request.method == "POST":
        user = request.POST.get("username")
        pwd = request.POST.get("password")
        user_obj = models.AdminInfo.objects.filter(username=user, password=pwd).first()
        if not user_obj:
            return render(request, "login.html", {"error": "用户名或密码错误！"})
        request.session["user"] = user_obj.username
        init_permission(user_obj, request)
        return redirect(reverse("index"))
        
    return render(request, "login.html")


def logout(request):
    """
    用户注销
    :param request:
    :return:
    """
    request.session.delete()
    return redirect(reverse("login"))

