from django.shortcuts import render, redirect
from django.urls import reverse
from crm import models
from crm.forms.classes import ClassesModelForm


def classes_list(request):
    """
    :param request:
    :return:
    """
    queryset = models.ClassList.objects.all()
    return render(request, 'classes_list.html', {'queryset': queryset, "username": request.session.get("user_info").get("name")})


def classes_add(request):
    """
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = ClassesModelForm()
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
    
    form = ClassesModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('classes_list'))
    return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})


def classes_edit(request, nid):
    """
    :param request:
    :param nid:
    :return:
    """
    obj = models.ClassList.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = ClassesModelForm(instance=obj)
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
    form = ClassesModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('classes_list'))
    else:
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})


def classes_del(request, nid):
    """
    :param request:
    :param nid:
    :return:
    """
    models.ClassList.objects.filter(id=nid).delete()
    return redirect(reverse('classes_list'))
