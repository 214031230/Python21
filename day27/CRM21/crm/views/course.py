from django.shortcuts import render, redirect
from django.urls import reverse
from crm import models
from crm.forms.course import CourseModelForm


def course_list(request):
    """
    课程列表
    参考部门列表
    :param request:
    :return:
    """
    queryset = models.Course.objects.all()
    return render(request, 'course_list.html',
                  {'queryset': queryset, "username": request.session.get("user_info").get("name")})


def course_add(request):
    """
    课程添加
    参考添加部门
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = CourseModelForm()
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})

    form = CourseModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('course_list'))
    return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})


def course_edit(request, nid):
    """
    课程编辑
    参考编辑部门
    :param request:
    :param nid:
    :return:
    """
    obj = models.Course.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = CourseModelForm(instance=obj)
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
    form = CourseModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('course_list'))
    else:
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})


def course_del(request, nid):
    """
    课程删除
    参考删除部门
    :param request:
    :param nid:
    :return:
    """
    models.Course.objects.filter(id=nid).delete()
    return redirect(reverse('course_list'))
