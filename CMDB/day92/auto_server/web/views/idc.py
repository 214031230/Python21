from django.shortcuts import render, redirect
from django.urls import reverse
from repository import models
from web import forms


def idc_list(request):
    """
    列表
    :param request: 
    :return: 
    """
    queryset_list = models.IDC.objects.all()
    return render(request, "web/idc_list.html", locals())


def idc_add(request):
    """
    添加
    :param request: 
    :return: 
    """
    if request.method == "POST":
        form_obj = forms.IdcModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("idc_list"))
        return render(request, "web/add_and_edit.html", locals())

    form_obj = forms.IdcModelForm()
    return render(request, "web/add_and_edit.html", locals())


def idc_edit(request, cid):
    """
    编辑
    :param request:
    :param cid: 表ID
    :return:
    """
    obj = models.IDC.objects.filter(id=cid).first()
    if request.method == "POST":
        form_obj = forms.IdcModelForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("idc_list"))
        return render(request, "web/add_and_edit.html")

    form_obj = forms.IdcModelForm(instance=obj)
    return render(request, "web/add_and_edit.html", locals())


def idc_del(request, cid):
    """
    删除
    :param request:
    :param cid: 表ID
    :return:
    """
    models.IDC.objects.filter(id=cid).delete()
    return redirect(reverse("idc_list"))
