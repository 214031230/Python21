from django.shortcuts import render, redirect
from django.urls import reverse
from crm import models
from crm.forms.user import UserModelForm


def user_list(request):
    """
    员工列表
    :param request:
    :return:
    """
    queryset = models.UserInfo.objects.all()
    return render(request, 'user_list.html', {'queryset': queryset})


def user_add(request):
    """
    员工添加
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_add.html', {'form': form})
    
    form = UserModelForm(data=request.POST)
    # 将用户提交的数据和Model中的字段进行校验
    if form.is_valid():
        form.save()
        return redirect(reverse('user_list'))
    else:
        return render(request, 'user_add.html', {'form': form})


def user_edit(request, nid):
    """
    编辑员工
    :param request:
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


def user_del(request, nid):
    """
    员工删除
    :param request:
    :param nid:
    :return:
    """
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect(reverse('user_list'))
