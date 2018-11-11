from django.shortcuts import render, redirect
from crm import models


def depart_list(request):
    """
    部门列表
    :param request:
    :return:
    """
    queryset = models.Department.objects.all()
    return render(request, 'depart_list.html',{'queryset':queryset})


def depart_add(request):
    """
    部门添加
    get:
        返回添加部门页面
    post：
        创建部门
    :param request: 
    :return: 
    """
    if request.method == "POST":
        title = request.POST.get("depart_title")
        models.Department.objects.create(title=title)
        return redirect("/depart/list")
    
    return render(request, "depart_add.html")