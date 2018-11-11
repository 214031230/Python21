from django.shortcuts import render, redirect,HttpResponse
from django.urls import reverse
from crm import models
from crm.forms.public import PublicCustomerModelForm


def public_customer_list(request):
    """
    公户列表
    :param request:
    :return:
    """
    if request.method == 'POST':
        id_list = request.POST.getlist('pk')
        current_user_id = request.session['user_info']['id']
        models.Customer.objects.filter(id__in=id_list).update(consultant_id=current_user_id)

    queryset = models.Customer.objects.filter(consultant__isnull=True)
    return render(request, 'public_customer_list.html', {'queryset': queryset})
    
def public_customer_add(request):
    """
    录入公户信息
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = PublicCustomerModelForm()
        return render(request, 'form.html', {'form': form})

    form = PublicCustomerModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('public_customer_list'))
    return render(request, 'form.html', {'form': form})
    
    
def public_customer_edit(request, nid):
    """
    :param request:
    :param nid:
    :return:
    """
    obj = models.Customer.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = PublicCustomerModelForm(instance=obj)
        return render(request, 'form.html', {'form': form})
    form = PublicCustomerModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('public_customer_list'))
    else:
        return render(request, 'form.html', {'form': form})
    
def public_customer_del(request, nid):
    """
    :param request:
    :param nid:
    :return:
    """
    models.Customer.objects.filter(id=nid).delete()
    return redirect(reverse('public_customer_list'))
