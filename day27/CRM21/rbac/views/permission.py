from django.shortcuts import render, redirect
from django.urls import reverse
from rbac import models
from rbac import forms


# Create your views here.
def permission_list(request):
    """
    增加权限
    :param request:
    :return:
    """
    queryset = models.Permission.objects.all()
    return render(request, 'rbac/permission_list.html',
                  {'queryset': queryset, "username": request.session.get("user_info").get("name")})


def permission_add(request):
    """
    增加权限
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = forms.PermissionModelForm()
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})

    form = forms.PermissionModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('permission_list'))
    return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})


def permission_edit(request, nid):
    """

    :param request:
    :return:
    """
    obj = models.Menu.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = forms.PermissionModelForm(instance=obj)
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
    form = forms.PermissionModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('permission_list'))
    else:
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})


def permission_del(request, nid):
    """

    :param request:
    :return:
    """
    models.Menu.objects.filter(id=nid).delete()
    return redirect(reverse('permission_list'))
