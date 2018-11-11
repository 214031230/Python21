from django.shortcuts import render, redirect
from django.urls import reverse
from crm import models
from crm.forms.customer import CustomerModelForm


def customer_list(request):
    """
    :param request:
    :return:
    """
    queryset = models.Customer.objects.all()
    return render(request, 'customer_list.html', {'queryset': queryset})


def customer_add(request):
    """
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = CustomerModelForm()
        return render(request, 'form.html', {'form': form})
    
    form = CustomerModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('customer_list'))
    return render(request, 'form.html', {'form': form})


def customer_edit(request, nid):
    """
    :param request:
    :param nid:
    :return:
    """
    obj = models.Customer.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = CustomerModelForm(instance=obj)
        return render(request, 'form.html', {'form': form})
    form = CustomerModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('customer_list'))
    else:
        return render(request, 'form.html', {'form': form})


def customer_del(request, nid):
    """
    :param request:
    :param nid:
    :return:
    """
    models.Customer.objects.filter(id=nid).delete()
    return redirect(reverse('customer_list'))
