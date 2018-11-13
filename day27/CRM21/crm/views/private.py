from django.shortcuts import render, redirect,HttpResponse
from django.urls import reverse
from crm import models
from crm.forms.private import PrivateCustomerModelForm


def private_customer_list(request):
    """
    私户列表
    POST：
        1. 取到需要'踢出到公户'的用户ID列表
        2. 更新id_list中的所有私户的顾问字段为空
    GET:
        1. 取到当前登录用户ID
        2. 获取顾问字段等于用户ID的所有私户，并按报名状态进行排序
        3. 返回给页面
    :param request:
    :return:
    """
    if request.method == 'POST':
        id_list = request.POST.getlist('pk')
        models.Customer.objects.filter(id__in=id_list).update(consultant=None)
    current_user_id = request.session['user_info']['id']
    queryset = models.Customer.objects.filter(consultant_id=current_user_id).order_by('-status')
    return render(request, 'private_customer_list.html', {'queryset': queryset, "username": request.session.get("user_info").get("name")})
    
    
def private_customer_add(request):
    """
    添加私户
    GET：
        1. 生成modelform对象（不包括顾问字段，顾问字段默认为当前登录用户）
        2. 返回给页面
    POST:
        1. 取到POST请求数据，使用mocelform进行创建
        2. 校验数据是否合格：成功则更新顾问ID为当前等于登录ID
        3. 保存数据，并跳转到私户列表
        4. 校验失败，返回错误页面
    录入私户信息
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = PrivateCustomerModelForm()
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})

    form = PrivateCustomerModelForm(data=request.POST)
    if form.is_valid():
        # 课程顾问我自己
        form.instance.consultant_id = request.session['user_info']['id']
        # form.instance.consultant = models.UserInfo.objects.get(id=request.session['user_info']['id'])
        form.save()
        return redirect(reverse('private_customer_list'))
    return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
    
    
def private_customer_edit(request, nid):
    """
    编辑私户
    GET:
        1. 取到需要编辑的私户ID
        2. 通过modelform返回给页面生成字段
    POST:
        1. 获取POST请求数据和私户对象进行modelform校验
        2. 校验成功，则更新数据，并跳转到私户列表
        3. 校验失败, 返回错误页面
    :param request:
    :param nid:
    :return:
    """
    obj = models.Customer.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = PrivateCustomerModelForm(instance=obj)
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
    form = PrivateCustomerModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('private_customer_list'))
    else:
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
