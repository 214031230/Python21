from django.shortcuts import render, redirect
from django.urls import reverse
from repository import models
from web import forms


def disk_list(request):
    """
    列表
    :param request: 
    :return: 
    """
    queryset_list = models.Disk.objects.all()
    return render(request, "web/disk_list.html", locals())


def disk_add(request):
    """
    添加
    :param request: 
    :return: 
    """
    if request.method == "POST":
        form_obj = forms.DiskModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("disk_list"))
        return render(request, "web/add_and_edit.html", locals())

    form_obj = forms.DiskModelForm()
    return render(request, "web/add_and_edit.html", locals())


def disk_edit(request, cid):
    """
    编辑
    :param request:
    :param cid: 表ID
    :return:
    """
    obj = models.Disk.objects.filter(id=cid).first()
    if request.method == "POST":
        form_obj = forms.DiskModelForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("disk_list"))
        return render(request, "web/add_and_edit.html")

    form_obj = forms.DiskModelForm(instance=obj)
    return render(request, "web/add_and_edit.html", locals())


def disk_del(request, cid):
    """
    删除
    :param request:
    :param cid: 表ID
    :return:
    """
    models.Disk.objects.filter(id=cid).delete()
    return redirect(reverse("disk_list"))
