from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from crm import models
from crm.forms.record import RecordModelForm


def record_list(request, nid):
    """
    跟进记录
    :param nid: 客户ID
    :param request:
    :return:
    """
    current_user_id = request.session['user_info']['id']

    exists = models.Customer.objects.filter(id=nid, consultant_id=current_user_id).exists()
    if not exists:
        return HttpResponse('只能查看自己客户的跟进记录')
    queryset = models.ConsultRecord.objects.filter(customer_id=nid)

    return render(request, 'record_list.html',
                  {'queryset': queryset, 'cid': nid, "username": request.session.get("user_info").get("name")})


def record_add(request, cid):
    """
    :param request:
    :param cid: 客户ID
    :return:
    """
    if request.method == 'GET':
        form = RecordModelForm()
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
    form = RecordModelForm(data=request.POST)
    if form.is_valid():
        form.instance.customer_id = cid
        form.instance.consultant_id = request.session['user_info']['id']

        form.save()
        return redirect(reverse('record_list', args=(cid,)))
    return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
