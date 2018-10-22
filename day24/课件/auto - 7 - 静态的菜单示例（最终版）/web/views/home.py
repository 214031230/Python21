from django.shortcuts import render,redirect
from web import models

def index(request):
    return render(request,'index.html')

def user(request):
    """
    用户列表
    :param request:
    :return:
    """
    user_list = models.User.objects.all()

    return render(request, 'user.html',{'user_list':user_list})

from django.forms import ModelForm
class UserModelForm(ModelForm):
    class Meta:
        model = models.User
        fields = "__all__"

        error_messages = {
            'name':{'required':'用户不能为空'}
        }

def add_user(request):
    """
    添加用户
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = UserModelForm()
    else:
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/web/user/')
    return render(request,'add_user.html',{'form':form})

def del_user(request,uid):
    """
    删除用户
    :param request:
    :param uid:
    :return:
    """
    models.User.objects.filter(id=uid).delete()
    return redirect('/web/user/')

def edit_user(request,uid):
    """
    编辑用户
    :param request:
    :param uid:
    :return:
    """
    obj = models.User.objects.filter(id=uid).first()

    if request.method == "GET":
        form = UserModelForm(instance=obj)
    else:
        form = UserModelForm(instance=obj,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/web/user/')
    return render(request, 'edit_user.html', {'form': form})

def order(request):
    return render(request, 'order.html')

def center(request):
    return render(request, 'center.html')