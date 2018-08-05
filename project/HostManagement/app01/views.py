from django.shortcuts import render, HttpResponse, redirect


def login(request):
    """
    用户登录
    :param request:
    :return: 登录成功：返回index页面 登录失败：登录页面
    """
    if request.method == "POST":
        username = request.POST.get("user")
        password = request.POST.get("pwd")
        if username == "spf" and password == "123":
            return redirect("/index/")
        else:
            return render(request, "login.html", {"login_status": "用户名密码错误"})
    else:
        return render(request, "login.html", {"login_status": ""})


def index(request):
    """
    index页面
    :param request:
    :return: 返回index页面
    """
    return render(request, "index.html")
