from django.shortcuts import render, redirect
from django.urls import reverse
from repository import models
from web import forms


def server_list(request):
    """
    列表
    :param request: 
    :return: 
    """
    queryset_list = models.Server.objects.all()
    return render(request, "web/server_list.html", locals())


def server_add(request):
    """
    添加
    :param request: 
    :return: 
    """
    if request.method == "POST":
        form_obj = forms.ServerModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("server_list"))
        return render(request, "web/add_and_edit.html", locals())

    form_obj = forms.ServerModelForm()
    return render(request, "web/add_and_edit.html", locals())


def server_edit(request, cid):
    """
    编辑
    :param request:
    :param cid: 表ID
    :return:
    """
    obj = models.Server.objects.filter(id=cid).first()
    if request.method == "POST":
        form_obj = forms.ServerModelForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("server_list"))
        return render(request, "web/add_and_edit.html")

    form_obj = forms.ServerModelForm(instance=obj)
    return render(request, "web/add_and_edit.html", locals())


def server_del(request, cid):
    """
    删除
    :param request:
    :param cid: 表ID
    :return:
    """
    models.Server.objects.filter(id=cid).delete()
    return redirect(reverse("server_list"))
