from django.shortcuts import render, redirect
from django.urls import reverse
from crm import models
from crm.forms.depart import DepartModelForm


def depart_list(request):
    """
    部门列表
    :param request:
    :return:
    """
    queryset = models.Department.objects.all()
    return render(request, 'depart_list.html', {'queryset': queryset})


def depart_add(request):
    """
    部门添加
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = DepartModelForm()
        return render(request, 'depart_add.html', {'form': form})
    
    form = DepartModelForm(data=request.POST)
    # 将用户提交的数据和Model中的字段进行校验
    if form.is_valid():
        form.save()
        return redirect(reverse('depart_list'))
    else:
        return render(request, 'depart_add.html', {'form': form})


def depart_edit(request, nid):
    """
    编辑部门
    :param request:
    :return:
    """
    obj = models.Department.objects.filter(id=nid).first()
    
    if request.method == 'GET':
        form = DepartModelForm(instance=obj)
        return render(request, 'depart_edit.html', {'form': form})
    form = DepartModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('depart_list'))
    else:
        return render(request, 'depart_edit.html', {'form': form})


def depart_del(request, nid):
    """
    部门删除
    :param request:
    :param nid:
    :return:
    """
    models.Department.objects.filter(id=nid).delete()
    return redirect(reverse('depart_list'))
