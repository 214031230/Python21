from django.shortcuts import render, redirect
from django.urls import reverse
from crm import models
from crm.forms.user import UserModelForm


def user_list(request):
    """
    用户列表
    参考部门列表
    :param request:
    :return:
    """
    queryset = models.UserInfo.objects.all()
    return render(request, 'user_list.html',
                  {'queryset': queryset, "username": request.session.get("user_info").get("name")})


def user_add(request):
    """
    用户添加
    参考添加部门
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})

    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('user_list'))
    return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})


def user_edit(request, nid):
    """
    用户编辑
    参考编辑部门
    :param request:
    :param nid:
    :return:
    """
    obj = models.UserInfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = UserModelForm(instance=obj)
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
    form = UserModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('user_list'))
    else:
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})


def user_del(request, nid):
    """
    用户删除
    参考删除部门
    :param request:
    :param nid:
    :return:
    """
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect(reverse('user_list'))
