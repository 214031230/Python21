from django.shortcuts import render, redirect,HttpResponse
from django.urls import reverse
from crm import models
from crm.forms.private import PrivateCustomerModelForm


def private_customer_list(request):
    """
    私户列表
    :param request:
    :return:
    """
    if request.method == 'POST':
        id_list = request.POST.getlist('pk')
        models.Customer.objects.filter(id__in=id_list).update(consultant=None)
    current_user_id = request.session['user_info']['id']
    queryset = models.Customer.objects.filter(consultant_id=current_user_id).order_by('-status')
    return render(request, 'private_customer_list.html', {'queryset': queryset, "username": request.session.get("user_info").get("name")})
    
    
def private_customer_add(request):
    """
    录入私户信息
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = PrivateCustomerModelForm()
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})

    form = PrivateCustomerModelForm(data=request.POST)
    if form.is_valid():
        # 课程顾问我自己
        form.instance.consultant_id = request.session['user_info']['id']
        # form.instance.consultant = models.UserInfo.objects.get(id=request.session['user_info']['id'])
        form.save()
        return redirect(reverse('private_customer_list'))
    return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
    
    
def private_customer_edit(request, nid):
    """
    :param request:
    :param nid:
    :return:
    """
    obj = models.Customer.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = PrivateCustomerModelForm(instance=obj)
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
    form = PrivateCustomerModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('private_customer_list'))
    else:
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
