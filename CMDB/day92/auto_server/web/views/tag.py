from django.shortcuts import render, redirect
from django.urls import reverse
from repository import models
from web import forms


def tag_list(request):
    """
    列表
    :param request: 
    :return: 
    """
    queryset_list = models.Tag.objects.all()
    return render(request, "web/tag_list.html", locals())


def tag_add(request):
    """
    添加
    :param request: 
    :return: 
    """
    if request.method == "POST":
        form_obj = forms.TagModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("tag_list"))
        return render(request, "web/add_and_edit.html", locals())

    form_obj = forms.TagModelForm()
    return render(request, "web/add_and_edit.html", locals())


def tag_edit(request, cid):
    """
    编辑
    :param request:
    :param cid: 表ID
    :return:
    """
    obj = models.Tag.objects.filter(id=cid).first()
    if request.method == "POST":
        form_obj = forms.TagModelForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("tag_list"))
        return render(request, "web/add_and_edit.html")

    form_obj = forms.TagModelForm(instance=obj)
    return render(request, "web/add_and_edit.html", locals())


def tag_del(request, cid):
    """
    删除
    :param request:
    :param cid: 表ID
    :return:
    """
    models.Tag.objects.filter(id=cid).delete()
    return redirect(reverse("tag_list"))
