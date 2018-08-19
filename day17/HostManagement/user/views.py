from django.shortcuts import render, redirect
from user import models
from user.public import Public
from functools import wraps
from django.utils.decorators import method_decorator
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def auth(f):
    """
    登录装饰器
    :param f:
    :return:
    """

    @wraps(f)
    def inner(request, *args, **kwargs):
        if not request.session.get("name"):
            path = request.path_info
            return redirect("/login/?path=%s" % path)
        else:
            return f(request, *args, **kwargs)

    return inner


def login(request):
    """
    用户登录
    :param request:
    :return: get:登录页面 post:登录认证
    """
    code = Public.code(4)
    if request.method == "POST":
        user = request.POST.get("username")
        pwd = request.POST.get("password")
        pwd = Public.md5(user, pwd)
        path = request.GET.get("path")
        if models.UserInfo.objects.filter(username=user, password=pwd).first():
            request.session["name"] = user
            if path:
                return redirect(path)
            else:
                return redirect("/platform/")
        else:
            if path:
                return redirect(request.GET.get("path"))
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误！", "code": code})
    return render(request, "login.html", {"code": code})


@auth
def platform(request):
    """
    管理后台页面
    :param request:
    :return:
    """
    user = request.session.get("name")
    return render(request, "index/platform.html", {"user": user})


@auth
def user_list(request):
    """
    用户管理页面
    :param request:
    :return:
    """
    user = request.session.get("name")
    data = models.UserInfo.objects.all()
    current_page = request.GET.get('p')
    paginator = Paginator(data, 5)
    try:
        posts = paginator.page(current_page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    if not current_page:
        current_page = 1
    start = (int(current_page) - 1) * 5
    return render(request, "user/user_list.html", {"user": user, "data": posts, "start": start})


@auth
def add_user(request):
    """
    创建用户
    :param request:
    :return: platform页面
    """
    user = request.session.get("name")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not username.strip():
            return render(request, "user/add_user.html", {"user_msg": "用户名不能为空！", "user": user})
        if not password.strip():
            return render(request, "user/add_user.html", {"pwd_msg": "密码不能为空！", "user": user})
        password = Public.md5(username, password)
        if not models.UserInfo.objects.filter(username=username).first():
            models.UserInfo.objects.create(username=username, password=password)
        else:
            return render(request, "user/add_user.html", {"msg": "用户名已经存在！", "user": user})
        return redirect("/user_list/")
    return render(request, "user/add_user.html", {"user": user})


@auth
def delete_user(request):
    """
    删除用户
    :param request:
    :return: platform页面
    """
    user_id = request.GET.get("id")
    models.UserInfo.objects.get(id=user_id).delete()
    return redirect("/user_list/")


@auth
def edit_user(request):
    """
    编辑用户
    :param request:
    :return:
    """
    user = request.session.get("name")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_id = request.POST.get("user_id")
        obj = models.UserInfo.objects.get(id=user_id)
        if not password.strip():
            return render(request, "user/edit_user.html",
                          {"username": obj.username, "user_id": obj.id, "pwd_msg": "密码不能为空！", "user": user})
        password = Public.md5(username, password)
        obj = models.UserInfo.objects.filter(username=username).first()
        obj.password = password
        obj.save()
        return redirect("/user_list/")
    user_id = request.GET.get("id")
    obj = models.UserInfo.objects.get(id=user_id)
    return render(request, "user/edit_user.html", {"username": obj.username, "user_id": obj.id, "user": user})


class BsLine(View):
    """
    业务线页面
    """

    @method_decorator(auth)
    def get(self, request):
        user = request.session.get("name")
        data = models.Product.objects.all()
        current_page = request.GET.get('p')
        paginator = Paginator(data, 5)
        try:
            posts = paginator.page(current_page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        if not current_page:
            current_page = 1
        start = (int(current_page) - 1) * 5
        return render(request, "bsline/bsline_list.html",
                      {"user": user, "data": posts, "start": start})


class AddBsline(View):
    """
    添加业务线
    """

    @method_decorator(auth)
    def get(self, request):
        user = request.session.get("name")
        return render(request, "bsline/add_bsline.html", {"user": user})

    def post(self, request):
        name = request.POST.get("name")
        if not models.Product.objects.filter(name=name).filter():
            models.Product.objects.create(name=name)
            return redirect("/bsline_list/")
        else:
            return render(request, "bsline/add_bsline.html", {"msg": "业务名已经存在！"})


class DeleteBsline(View):
    """
    删除业务线
    """

    @method_decorator(auth)
    def get(self, request):
        bsline_id = request.GET.get("id")
        models.Product.objects.filter(id=bsline_id).delete()
        return redirect("/bsline_list/")


class EditBsline(View):
    """
    编辑业务线名称
    """

    @method_decorator(auth)
    def get(self, request):
        user = request.session.get("name")
        bsline_id = request.GET.get("id")
        bsline_name = models.Product.objects.filter(id=bsline_id).first()
        return render(request, "bsline/edit_bsline.html", {"names": bsline_name.name, "user": user})

    def post(self, request):
        name = request.POST.get("name")
        bsline_id = request.GET.get("id")
        obj = models.Product.objects.filter(id=bsline_id).first()
        if not models.Product.objects.filter(name=name).first():
            obj.name = name
            obj.save()
            return redirect("/bsline_list/")
        else:
            bsline_id = request.GET.get("id")
            bsline_name = models.Product.objects.filter(id=bsline_id).first()
            return render(request, "bsline/edit_bsline.html", {"msg": "业务名称已经存在", "name": bsline_name.name})


class HostList(View):
    """
    查看主机列表
    """

    @method_decorator(auth)
    def get(self, request):
        user = request.session.get("name")
        data = models.HostInfo.objects.all()
        current_page = request.GET.get('p')
        paginator = Paginator(data, 5)
        try:
            posts = paginator.page(current_page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        if not current_page:
            current_page = 1
        start = (int(current_page) - 1) * 5
        return render(request, "host/host_list.html",
                      {"user": user, "data": posts, "start": start})


class AddHost(View):
    """
    添加主机
    """

    @method_decorator(auth)
    def get(self, request):
        bsline_list = models.Product.objects.all()
        user = request.session.get("name")
        return render(request, "host/add_host.html", {"bsline_list": bsline_list, "user": user})

    def post(self, request):
        ip = request.POST.get("ip")
        hostname = request.POST.get("hostname")
        bsline_id = request.POST.get("bsline_name")
        bsline_list = models.Product.objects.all()
        if not models.HostInfo.objects.filter(ip=ip).filter():
            models.HostInfo.objects.create(ip=ip, hostname=hostname, product_id=bsline_id)
            return redirect("/host_list/")
        else:
            return render(request, "host/add_host.html", {"msg": "主机已经存在！", "bsline_list": bsline_list})


class DeleteHost(View):
    """
    删除主机
    """

    @method_decorator(auth)
    def get(self, request):
        host_id = request.GET.get("id")
        models.HostInfo.objects.filter(id=host_id).delete()
        return redirect("/host_list/")


class EditHost(View):
    """
    编辑主机
    """

    @method_decorator(auth)
    def get(self, request):
        user = request.session.get("name")
        bsline_list = models.Product.objects.all()
        host_id = request.GET.get("id")
        obj = models.HostInfo.objects.filter(id=host_id).first()
        return render(request, "host/edit_host.html/", {"bsline_list": bsline_list, "obj": obj, "user": user})

    def post(self, request):
        host_id = request.GET.get("id")
        hostname = request.POST.get("hostname")
        bsline_id = request.POST.get("bsline_name")
        obj = models.HostInfo.objects.filter(id=host_id).first()
        obj.hostname = hostname
        obj.product_id = bsline_id
        obj.save()
        return redirect("/host_list")


# def page_not_found(request):
#     """
#     自定义404页面
#     :param request:
#     :return:
#     """
#     return render(request, "404.html")


def init():
    """
    初始化数据库
    :return:
    """
    password = Public.md5("admin", "123456")
    if not models.UserInfo.objects.filter(username="admin").first():
        models.UserInfo.objects.create(username="admin", password=password)


init()
