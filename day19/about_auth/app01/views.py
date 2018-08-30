from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def login(request):
    """
    用户登录验证，使用auth
    :param request:
    :return:
    """
    if request.method == "POST":
        next = request.GET.get("next", "/index/")
        username = request.POST.get("username")
        password = request.POST.get("password")
        status = auth.authenticate(request, username=username, password=password)
        if status:
            auth.login(request, status)
            return redirect(next)
        else:
            return render(request, "login.html", {"error_msg": "用户名或者密码错误"})
    return render(request, "login.html")


@login_required
def index(request):
    """
    后台首页
    :param request: 
    :return: 
    """
    return render(request, "index.html")


def reg(request):
    """
    注册页面
    :param request: 
    :return: 
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        User.objects.create_user(username=username, password=password)
        return redirect("/login/")
    return render(request, "reg.html")