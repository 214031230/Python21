from django.shortcuts import render, HttpResponse
from app01 import models
# Create your views here.


def ajax_test(request):
    return render(request, "ajax_test.html")


def calc(request):
    print(request.GET)
    print(request.POST)
    i1 = int(request.POST.get("i1"))
    i2 = int(request.POST.get("i2"))

    print(request.POST.get("ooxx"))

    ret = i1 + i2
    return HttpResponse(ret)


def reg(request):

    return render(request, "reg.html")


def check_username(request):
    username = request.GET.get("name")
    is_exist = models.UserInfo.objects.filter(name=username)
    obj = models.UserInfo.objects.first()
    print(obj)
    if is_exist:
        res = "用户名已经存在"
    else:
        res = ""

    return HttpResponse(res)

