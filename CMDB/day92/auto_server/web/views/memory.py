from django.shortcuts import render, redirect
from django.urls import reverse
from repository import models
from web import forms


def memory_list(request):
    """
    列表
    :param request: 
    :return: 
    """
    queryset_list = models.Memory.objects.all()
    return render(request, "web/memory_list.html", locals())


def memory_add(request):
    """
    添加
    :param request: 
    :return: 
    """
    if request.method == "POST":
        form_obj = forms.MemoryModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("memory_list"))
        return render(request, "web/add_and_edit.html", locals())

    form_obj = forms.MemoryModelForm()
    return render(request, "web/add_and_edit.html", locals())


def memory_edit(request, cid):
    """
    编辑
    :param request:
    :param cid: 表ID
    :return:
    """
    obj = models.Memory.objects.filter(id=cid).first()
    if request.method == "POST":
        form_obj = forms.MemoryModelForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("memory_list"))
        return render(request, "web/add_and_edit.html")

    form_obj = forms.MemoryModelForm(instance=obj)
    return render(request, "web/add_and_edit.html", locals())


def memory_del(request, cid):
    """
    删除
    :param request:
    :param cid: 表ID
    :return:
    """
    models.Memory.objects.filter(id=cid).delete()
    return redirect(reverse("memory_list"))
