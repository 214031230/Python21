from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from crm import models
from crm.forms.public import PublicCustomerModelForm


def public_customer_list(request):
    """
    公户列表
    POST:
        1. 获取需要'申请到我的私户'的用户ID列表
        2. 获取当前登录的用户ID
        3. 更新id_list中的所有公户为当前用户的私户
    GET:
        1. 获取用户顾问字段为空的所有用户
        2. 返回页面进行展示
    :param request:
    :return:
    """
    if request.method == 'POST':
        id_list = request.POST.getlist('pk')
        current_user_id = request.session['user_info']['id']
        models.Customer.objects.filter(id__in=id_list).update(consultant_id=current_user_id)

    queryset = models.Customer.objects.filter(consultant__isnull=True)
    return render(request, 'public_customer_list.html',
                  {'queryset': queryset, "username": request.session.get("user_info").get("name")})


def public_customer_add(request):
    """
    添加公户
    GET:
        1. 生成modelform对象（不包括顾问字段和用户状态已报名或未报名，录入公户不能选择顾问）
        2. 返回modelform对象给页面，生成标签
    POST:
        1. 取到POST请求数据，进行modelform校验
        2. 校验成功， 跳转到公户列表
        2. 校验失败： 返回错误页面
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = PublicCustomerModelForm()
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})

    form = PublicCustomerModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('public_customer_list'))
    return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})


def public_customer_edit(request, nid):
    """
    编辑公户
    GET:
        1. 取到需要编辑的公户对象
        2. 使用modelform返回编辑页面
    POST：
        1. 获取POST对象和用户对象进行modelform校验
        2. 校验成功： 更新数据，并跳转到公户列表
        3. 校验失败： 返回错误信息给编辑页面
    :param request:
    :param nid:
    :return:
    """
    obj = models.Customer.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = PublicCustomerModelForm(instance=obj)
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
    form = PublicCustomerModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('public_customer_list'))
    else:
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})


def public_customer_del(request, nid):
    """
    删除公户
    :param request:
    :param nid:
    :return:
    """
    models.Customer.objects.filter(id=nid).delete()
    return redirect(reverse('public_customer_list'))
