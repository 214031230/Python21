from django.shortcuts import render, redirect
from django.urls import reverse
from repository import models
from web import forms


def user_list(request):
    """
    列表
    :param request: 
    :return: 
    """
    queryset_list = models.UserProfile.objects.all()
    return render(request, "web/user_list.html", locals())


def user_add(request):
    """
    添加
    :param request: 
    :return: 
    """
    if request.method == "POST":
        form_obj = forms.UserProfileModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("user_list"))
        return render(request, "web/add_and_edit.html", locals())

    form_obj = forms.UserProfileModelForm()
    return render(request, "web/add_and_edit.html", locals())


def user_edit(request, cid):
    """
    编辑
    :param request:
    :param cid: 表ID
    :return:
    """
    obj = models.UserProfile.objects.filter(id=cid).first()
    if request.method == "POST":
        form_obj = forms.UserProfileModelForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("user_list"))
        return render(request, "web/add_and_edit.html")

    form_obj = forms.UserProfileModelForm(instance=obj)
    return render(request, "web/add_and_edit.html", locals())


def user_del(request, cid):
    """
    删除
    :param request:
    :param cid: 表ID
    :return:
    """
    models.UserProfile.objects.filter(id=cid).delete()
    return redirect(reverse("user_list"))
