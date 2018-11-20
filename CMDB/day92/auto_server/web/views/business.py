from django.shortcuts import render, redirect
from django.urls import reverse
from repository import models
from web import forms


def business_list(request):
    """
    列表
    :param request: 
    :return: 
    """
    queryset_list = models.BusinessUnit.objects.all()
    return render(request, "web/business_list.html", locals())


def business_add(request):
    """
    添加
    :param request: 
    :return: 
    """
    if request.method == "POST":
        form_obj = forms.BusinessUnitModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("business_list"))
        return render(request, "web/add_and_edit.html", locals())

    form_obj = forms.BusinessUnitModelForm()
    return render(request, "web/add_and_edit.html", locals())


def business_edit(request, cid):
    """
    编辑
    :param request:
    :param cid: 表ID
    :return:
    """
    obj = models.BusinessUnit.objects.filter(id=cid).first()
    if request.method == "POST":
        form_obj = forms.BusinessUnitModelForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("business_list"))
        return render(request, "web/add_and_edit.html")

    form_obj = forms.BusinessUnitModelForm(instance=obj)
    return render(request, "web/add_and_edit.html", locals())


def business_del(request, cid):
    """
    删除
    :param request:
    :param cid: 表ID
    :return:
    """
    models.BusinessUnit.objects.filter(id=cid).delete()
    return redirect(reverse("business_list"))
