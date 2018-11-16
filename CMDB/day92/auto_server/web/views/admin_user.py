from django.shortcuts import render, redirect
from django.urls import reverse
from repository import models
from web import forms


def admin_user_list(request):
    """
    列表
    :param request: 
    :return: 
    """
    queryset_list = models.AdminInfo.objects.all()
    return render(request, "web/admin_user_list.html", locals())


def admin_user_add(request):
    """
    添加
    :param request: 
    :return: 
    """
    if request.method == "POST":
        form_obj = forms.AdminInfoModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("admin_user_list"))
        return render(request, "web/add_and_edit.html", locals())

    form_obj = forms.AdminInfoModelForm()
    return render(request, "web/add_and_edit.html", locals())


def admin_user_edit(request, cid):
    """
    编辑
    :param request:
    :param cid: 表ID
    :return:
    """
    obj = models.AdminInfo.objects.filter(id=cid).first()
    if request.method == "POST":
        form_obj = forms.AdminInfoModelForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("admin_user_list"))
        return render(request, "web/add_and_edit.html")

    form_obj = forms.AdminInfoModelForm(instance=obj)
    return render(request, "web/add_and_edit.html", locals())


def admin_user_del(request, cid):
    """
    删除
    :param request:
    :param cid: 表ID
    :return:
    """
    models.AdminInfo.objects.filter(id=cid).delete()
    return redirect(reverse("admin_user_list"))
