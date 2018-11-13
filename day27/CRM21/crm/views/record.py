from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from crm import models
from crm.forms.record import RecordModelForm


def record_list(request, nid):
    """
    跟进记录
    1. 取到当前登录用户的ID
    2. 获取客户信息，但顾问必须是自己的。
    3. 如果顾问不是自己，则返回错误信息
    4. 获取客户ID对应的所有根据记录
    5. 返回根据记录到页面
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
    增加跟进记录
    GET:
        1. 生成modelform对象返回给页面生成标签
    POST:
        1. 获取用户条提交的POST数据给modelform进行格式校验
        2. 校验成功， 修改客户ID为当前客户ID， 修改顾问ID为当前登录用户ID。保存数据，跳转到跟进记录列表，需要传递ID
        3. 校验失败, 返回错误页面
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
