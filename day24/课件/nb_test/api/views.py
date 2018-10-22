from django.shortcuts import render, HttpResponse, redirect
from api import models
from rbac import models as rbac_model
from rbac.service.permission import init_permission
from api.forms import ApiModelForm, ApplicationModelForm


def login(request):
    """
    用户登录
        1. Get请求: 返回用户登录页面
        2. Post请求:
            1. 获取form表单的用户名和密码
            2. 去数据库中检测用户名和密码
            3. 如果检测失败则返回用户名密码错误
            4. 成功则初始化用户信息（init_permission : 获取用户权限和菜单存储到session中）
            5. 跳转到应用列表页面
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'api/login.html')

    user = request.POST.get('user')
    pwd = request.POST.get('pwd')

    user = rbac_model.UserInfo.objects.filter(username=user, password=pwd).first()
    if not user:
        return render(request, 'api/login.html', {'msg': '用户名或密码错误'})
    init_permission(user, request)

    return redirect('/api/app/list/')


def logout(request):
    """
    用户注销按钮
        1. 删除用户的所有session
        2. 跳转到用户登录页面
    :param request:
    :return:
    """
    request.session.delete()
    return redirect("/api/login/")


def app_list(request):
    """
    应用列表
    :param request:
    :return:
    """
    app_queryset = models.Application.objects.all()
    return render(request, 'api/app_list.html', {'app_queryset': app_queryset})


def app_add(request):
    """
    添加应用
    :param request:
    :return:
    """
    form_obj = ApplicationModelForm()
    if request.method == "POST":
        form_obj = ApplicationModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect("/api/app/list/")
    
    return render(request, "api/app_add.html", locals())


def app_edit(request, nid):
    """
    编辑应用
    :param request:
    :return:
    """
    app_obj = models.Application.objects.filter(id=nid).first()
    form_obj = ApplicationModelForm(instance=app_obj)
    if request.method == "POST":
        form_obj = ApplicationModelForm(request.POST, instance=app_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect("/api/app/list/")
    return render(request, "api/app_edit.html", locals())


def app_del(request, nid):
    """
    删除应用
    :param request:
    :return:
    """
    return HttpResponse('删除应用')


def api_list(request):
    """
    接口列表
    :param request:
    :return:
    """
    return HttpResponse('api列表')


def api_add(request):
    """
    添加接口
    :param request:
    :return:
    """
    return HttpResponse('添加api')


def api_edit(request, nid):
    """
    编辑接口
    :param request:
    :return:
    """
    return HttpResponse('编辑api')


def api_del(request, nid):
    """
    删除接口
    :param request:
    :return:
    """
    return HttpResponse('删除api')
