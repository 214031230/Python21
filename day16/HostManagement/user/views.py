from django.shortcuts import render


def login(request):
    """
    用户登录
    :param request:
    :return: get:登录页面 post:登录认证
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

    return render(request, "login.html")

