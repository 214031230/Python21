from django.shortcuts import render,redirect
from django.urls import reverse
from crm import models
from crm.forms.user import UserModelForm

def user_list(request):
    """
    用户列表
    :param request:
    :return:
    """
    queryset = models.UserInfo.objects.all()
    return render(request,'user_list.html',{'queryset':queryset})


def user_add(request):
    """
    用户添加
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = UserModelForm()
        return render(request,'user_add.html',{'form':form})
    
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('user_list'))
    return render(request, 'user_add.html', {'form': form})


def user_edit(request,nid):
    """
    用户编辑
    :param request:
    :param nid:
    :return:
    """
    obj = models.UserInfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = UserModelForm(instance=obj)
        return render(request, 'user_edit.html', {'form': form})
    form = UserModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('user_list'))
    else:
        return render(request, 'user_edit.html', {'form': form})
    
    
def user_del(request,nid):
    """
    用户删除
    :param request:
    :param nid:
    :return:
    """
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect(reverse('user_list'))