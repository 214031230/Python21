from django.shortcuts import render,HttpResponse,redirect
from rbac.service.permission import init_permission
from rbac import models

def login(request):
    """
    用户登录
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request,'app01/login.html')
    
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    

    user = models.UserInfo.objects.filter(username=user,password=pwd).first()
    if not user:
        return render(request, 'app01/login.html',{'msg':'用户名或密码错误'})
    init_permission(user,request)
    
    return redirect('/app01/user/')
    
    
def user_list(request):
    
    return render(request,'app01/user_list.html')

def center(request):
    return render(request,'app01/center.html')