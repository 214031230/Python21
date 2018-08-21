from django.shortcuts import render, redirect
from app01 import models

# Create your views here.


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("password")
    obj = models.User.objects.filter(username=username, password=password)
    if obj.exists():
        request.session["spf"] = 123
        return redirect("/platform/")
    else:
        return render(request, "login.html", {"msg": "用户名或者密码错误！"})
    
    
def platform(request):
    print(request.session.get("spf"))
    print(request.session.session_key)
    return render(request, "platform.html")