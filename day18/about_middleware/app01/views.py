from django.shortcuts import render, redirect
from app01 import models


def auth(f):
    """
    登录验证装饰器
    :param f:
    :return:
    """

    def inner(request, *args, **kwargs):
        if request.session.get("spf"):
            return f(request, *args, **kwargs)
        else:
            return redirect("/login/?path={}".format(request.path_info))

    return inner


def login(request):
    """
    用户登录
    :param request: 
    :return: 
    """
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("password")
    path = request.GET.get("path")
    obj = models.User.objects.filter(username=username, password=password)
    if obj.exists():
        request.session["spf"] = 123
        if path:
            return redirect(path)
        else:
            return redirect("/platform/")
    else:
        return render(request, "login.html", {"msg": "用户名或者密码错误"})


@auth
def logout(request):
    """
    登出
    :param request: 
    :return: 
    """
    request.session.flush()
    return redirect("/login/")


@auth
def platform(request):
    """
    后台首页
    :param request:
    :return:
    """
    return render(request, "platform.html")
