from django.shortcuts import render, redirect
from django.urls import reverse
from crm import models
from crm.forms.school import SchoolModelForm


def school_list(request):
    """
    校区列表
    参考部门列表
    :param request:
    :return:
    """
    queryset = models.School.objects.all()
    return render(request, 'school_list.html',
                  {'queryset': queryset, "username": request.session.get("user_info").get("name")})


def school_add(request):
    """
    添加校区
    参考添加校区
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = SchoolModelForm()
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})

    form = SchoolModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('school_list'))
    return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})


def school_edit(request, nid):
    """
    编辑校区
    参考编辑校区
    :param request:
    :param nid:
    :return:
    """
    obj = models.School.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = SchoolModelForm(instance=obj)
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
    form = SchoolModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('school_list'))
    else:
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})


def school_del(request, nid):
    """
    校区删除
    参考删除部门
    :param request:
    :param nid:
    :return:
    """
    models.School.objects.filter(id=nid).delete()
    return redirect(reverse('school_list'))
