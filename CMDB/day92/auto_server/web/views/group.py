from django.shortcuts import render, redirect
from django.urls import reverse
from repository import models
from web import forms


def group_list(request):
    """
    列表
    :param request: 
    :return: 
    """
    queryset_list = models.UserGroup.objects.all()
    return render(request, "web/user_group.html", locals())


def group_add(request):
    """
    添加
    :param request: 
    :return: 
    """
    if request.method == "POST":
        form_obj = forms.UserGroupModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("group_list"))
        return render(request, "web/add_and_edit.html", locals())

    form_obj = forms.UserGroupModelForm()
    return render(request, "web/add_and_edit.html", locals())


def group_edit(request, cid):
    """
    编辑
    :param request:
    :param cid: 表ID
    :return:
    """
    obj = models.UserGroup.objects.filter(id=cid).first()
    if request.method == "POST":
        form_obj = forms.UserGroupModelForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("group_list"))
        return render(request, "web/add_and_edit.html")

    form_obj = forms.UserGroupModelForm(instance=obj)
    return render(request, "web/add_and_edit.html", locals())


def group_del(request, cid):
    """
    删除
    :param request:
    :param cid: 表ID
    :return:
    """
    models.UserGroup.objects.filter(id=cid).delete()
    return redirect(reverse("group_list"))
