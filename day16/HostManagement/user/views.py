from django.shortcuts import render, HttpResponse, redirect
from user import models
from user.public import Public
import os


def login(request):
    """
    用户登录
    :param request:
    :return: get:登录页面 post:登录认证
    """
    if request.method == "POST":
        user = request.POST.get("username")
        pwd = request.POST.get("password")
        pwd = Public.md5(user, pwd)
        try:
            obj = models.UserInfo.objects.get(username=user)
        except Exception:
            return render(request, "user/login.html", {"msg": "用户名或密码错误！"})
        if obj.username == user and obj.password == pwd:
            return redirect("/platform/")
        else:
            return render(request, "user/login.html", {"msg": "用户名或密码错误！"})
    return render(request, "user/login.html")


def platform(request):
    """
    管理后台页面
    :param request:
    :return:
    """
    data = models.UserInfo.objects.all()
    return render(request, "platform.html", {"userinfo": data})


def user_list(request):
    """
    用户管理页面
    :param request:
    :return:
    """
    data = models.UserInfo.objects.all()
    return render(request, "user/user_list.html", {"userinfo": data})


def add_user(request):
    """
    创建用户
    :param request:
    :return: platform页面
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not username.strip():
            return render(request, "user/add_user.html", {"user_msg": "用户名不能为空！"})
        if not password.strip():
            return render(request, "user/add_user.html", {"pwd_msg": "密码不能为空！"})
        password = Public.md5(username, password)
        try:
            models.UserInfo.objects.create(username=username, password=password)
        except Exception as e:
            print(e)
            return render(request, "user/add_user.html", {"msg": "用户名已经存在！"})
        return redirect("/user_list/")
    return render(request, "user/add_user.html")


def delete_user(request):
    """
    删除用户
    :param request:
    :return: platform页面
    """
    user_id = request.GET.get("id")
    models.UserInfo.objects.get(id=user_id).delete()
    return redirect("/user_list/")


def edit_user(request):
    """
    编辑用户
    :param request:
    :return:
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_id = request.POST.get("user_id")
        obj = models.UserInfo.objects.get(id=user_id)
        if not username.strip():
            return render(request, "user/edit_user.html",
                          {"username": obj.username, "user_id": obj.id, "user_msg": "用户名不能为空！"})
        if not password.strip():
            return render(request, "user/edit_user.html",
                          {"username": obj.username, "user_id": obj.id, "pwd_msg": "密码不能为空！"})
        password = Public.md5(username, password)
        try:
            obj = models.UserInfo.objects.get(id=user_id)
            obj.username = username
            obj.password = password
            obj.save()
        except Exception:
            return render(request, "user/edit_user.html", {"msg": "用户名已经存在！"})
        return redirect("/user_list/")

    user_id = request.GET.get("id")
    obj = models.UserInfo.objects.get(id=user_id)
    return render(request, "user/edit_user.html", {"username": obj.username, "user_id": obj.id})


def host_list(request):
    """
    主机列表
    :param request: 
    :return: 
    """
    return render(request, "host/host_list.html")


def init(request):
    """
    初始化数据库
    :param request:
    :return:
    """
    if request.method == "POST":
        password = Public.md5("admin", "123456")
        try:
            os.chdir(os.path.dirname(os.path.dirname(__file__)))
            os.popen("python manage.py  makemigrations").read()
            os.popen("python manage.py  migrate").read()
            models.UserInfo.objects.create(username="admin", password=password)
            os.popen("python manage.py  makemigrations").read()
            ret2 = os.popen("python manage.py  migrate").read()
            return render(request, "init.html", {"msg": "初始化成功", "status": "btn-success"})
        except Exception:
            pass
        return render(request, "init.html", {"msg": "初始化成功", "status": "btn-success"})

    return render(request, "init.html", {"msg": "初始化数据库", "status": "btn-danger"})
