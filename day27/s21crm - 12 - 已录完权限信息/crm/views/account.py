from django.shortcuts import render,redirect
from django.urls import reverse
from crm import models
from crm.utils.md5 import md5

from rbac.service.permission import init_permission

def login(request):
    """
    用户登录
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request,'login.html')
    
    user = request.POST.get('username')
    pwd = md5(request.POST.get('password'))
    
    user_object = models.UserInfo.objects.filter(username=user,password=pwd).first()
    if not user_object:
        return render(request, 'login.html',{'error':'用户名或密码错误'})
    
    request.session['user_info'] = {'id':user_object.id,'name':user_object.username}

    init_permission(user_object,request)
    
    return redirect(reverse('index'))

def index(request):
    return render(request,'index.html')