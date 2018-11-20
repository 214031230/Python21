from django.shortcuts import render, redirect
from django.urls import reverse
from repository import models
from web import forms


def server_record_list(request):
    """
    列表
    :param request: 
    :return: 
    """
    queryset_list = models.ServerRecord.objects.all()
    return render(request, "web/server_record_list.html", locals())


# def server_record_add(request):
#     """
#     添加
#     :param request:
#     :return:
#     """
#     if request.method == "POST":
#         form_obj = forms.ServerRecordModelForm(request.POST)
#         if form_obj.is_valid():
#             form_obj.save()
#             return redirect(reverse("server_record_list"))
#         return render(request, "web/add_and_edit.html", locals())
#
#     form_obj = forms.ServerRecordModelForm()
#     return render(request, "web/add_and_edit.html", locals())
#
#
# def server_record_edit(request, cid):
#     """
#     编辑
#     :param request:
#     :param cid: 表ID
#     :return:
#     """
#     obj = models.ServerRecord.objects.filter(id=cid).first()
#     if request.method == "POST":
#         form_obj = forms.ServerRecordModelForm(request.POST, instance=obj)
#         if form_obj.is_valid():
#             form_obj.save()
#             return redirect(reverse("server_record_list"))
#         return render(request, "web/add_and_edit.html")
#
#     form_obj = forms.ServerRecordModelForm(instance=obj)
#     return render(request, "web/add_and_edit.html", locals())
#
#
# def server_record_del(request, cid):
#     """
#     删除
#     :param request:
#     :param cid: 表ID
#     :return:
#     """
#     models.ServerRecord.objects.filter(id=cid).delete()
#     return redirect(reverse("server_record_list"))
