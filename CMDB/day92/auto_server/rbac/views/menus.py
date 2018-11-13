from django.shortcuts import render, redirect
from django.urls import reverse
from rbac import models
from rbac import forms


# Create your views here.
def menus_list(request):
    """
    菜单列表
    参考部门列表
    :param request:
    :return:
    """
    queryset = models.Menu.objects.all()
    return render(request, 'rbac/menu_list.html',
                  {'queryset': queryset, "username": request.session.get("user_info").get("name")})


def menus_add(request):
    """
    增加菜单
    参考增加部门
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = forms.MenusModelForm()
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})

    form = forms.MenusModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('menus_list'))
    return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})


def menus_edit(request, nid):
    """
    编辑菜单
    参考编辑部门
    :param request:
    :return:
    """
    obj = models.Menu.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = forms.MenusModelForm(instance=obj)
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
    form = forms.MenusModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('menus_list'))
    else:
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})


def menus_del(request, nid):
    """
    删除菜单
    参考删除部门
    :param request:
    :return:
    """
    models.Menu.objects.filter(id=nid).delete()
    return redirect(reverse('menus_list'))
