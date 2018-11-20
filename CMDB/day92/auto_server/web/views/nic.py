from django.shortcuts import render, redirect
from django.urls import reverse
from repository import models
from web import forms


def nic_list(request):
    """
    列表
    :param request: 
    :return: 
    """
    queryset_list = models.NIC.objects.all()
    return render(request, "web/nic_list.html", locals())


def nic_add(request):
    """
    添加
    :param request: 
    :return: 
    """
    if request.method == "POST":
        form_obj = forms.NicModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("nic_list"))
        return render(request, "web/add_and_edit.html", locals())

    form_obj = forms.NicModelForm()
    return render(request, "web/add_and_edit.html", locals())


def nic_edit(request, cid):
    """
    编辑
    :param request:
    :param cid: 表ID
    :return:
    """
    obj = models.NIC.objects.filter(id=cid).first()
    if request.method == "POST":
        form_obj = forms.NicModelForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("nic_list"))
        return render(request, "web/add_and_edit.html")

    form_obj = forms.NicModelForm(instance=obj)
    return render(request, "web/add_and_edit.html", locals())


def nic_del(request, cid):
    """
    删除
    :param request:
    :param cid: 表ID
    :return:
    """
    models.NIC.objects.filter(id=cid).delete()
    return redirect(reverse("nic_list"))
