from django.shortcuts import render, redirect
from django.urls import reverse
from crm import models
from crm.forms.depart import DepartModelForm


def depart_list(request):
    """
    部门列表
    1. 取到所有部门信息
    2. 把部门信息返回给页面进行展示
    :param request:
    :return:
    """
    queryset = models.Department.objects.all()
    return render(request, 'depart_list.html', {'queryset': queryset, "username": request.session.get("user_info").get("name")})


def depart_add(request):
    """
    部门添加
    GET:
        1. 生成modelform对象
        2. 返回对象给页面生成标签
    POST：
        1. 拿到页面通过POST提交过来的数据进行modelform校验
        2. 校验成功，保存数据，并跳转到部门列表
        3. 校验失败，则通过modelform返回错误信息给页面
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = DepartModelForm()
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
    
    form = DepartModelForm(data=request.POST)
    # 将用户提交的数据和Model中的字段进行校验
    if form.is_valid():
        form.save()
        return redirect(reverse('depart_list'))
    else:
        return render(request, 'form.html', {'form': form})


def depart_edit(request, nid):
    """
    编辑部门
    GET：
        1. 取到需要编辑的部门对象
        2. 通过modelform把部门对象返回给页面展示
    POST：
        1. 把页面POST数据和部门对象传给modelform进行校验
        2. 校验成功，更新
        2. 校验失败，通过modelform返回错误信息给页面
    :param request:
    :return:
    """
    obj = models.Department.objects.filter(id=nid).first()
    
    if request.method == 'GET':
        form = DepartModelForm(instance=obj)
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
    form = DepartModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('depart_list'))
    else:
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})


def depart_del(request, nid):
    """
    部门删除
    1. 根据部门ID删除，删除成功跳转到部门列表
    :param request:
    :param nid:
    :return:
    """
    models.Department.objects.filter(id=nid).delete()
    return redirect(reverse('depart_list'))
