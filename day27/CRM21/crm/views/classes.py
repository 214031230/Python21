from django.shortcuts import render, redirect
from django.urls import reverse
from crm import models
from crm.forms.classes import ClassesModelForm


def classes_list(request):
    """
    班级列表
    参考部门列表
    :param request:
    :return:
    """
    queryset = models.ClassList.objects.all()
    return render(request, 'classes_list.html', {'queryset': queryset, "username": request.session.get("user_info").get("name")})


def classes_add(request):
    """
    添加班级
    参考添加部门
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = ClassesModelForm()
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
    
    form = ClassesModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('classes_list'))
    return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})


def classes_edit(request, nid):
    """
    编辑班级
    参考编辑部门
    :param request:
    :param nid:
    :return:
    """
    obj = models.ClassList.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = ClassesModelForm(instance=obj)
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
    form = ClassesModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('classes_list'))
    else:
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})


def classes_del(request, nid):
    """
    删除班级
    参考删除部门
    :param request:
    :param nid:
    :return:
    """
    models.ClassList.objects.filter(id=nid).delete()
    return redirect(reverse('classes_list'))
