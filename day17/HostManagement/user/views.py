from django.shortcuts import render, redirect
from user import models
from user.public import Public
from functools import wraps
from django.utils.decorators import method_decorator
from django.views import View


def auth(f):
    """
    登录装饰器
    :param f:
    :return:
    """

    @wraps(f)
    def inner(re, *args, **kwargs):
        if not re.session.get("name"):
            path = re.path_info
            return redirect("/login/?path=%s" % path)
        else:
            return f(re, *args, **kwargs)

    return inner


def login(request):
    """
    用户登录
    :param request:
    :return: get:登录页面 post:登录认证
    """
    code = Public.code(5)
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
    data = models.UserInfo.objects.all()
    return render(request, "index/platform.html", {"userinfo": data, "user": user})


@auth
def user_list(request):
    """
    用户管理页面
    :param request:
    :return:
    """
    user = request.session.get("name")
    data = models.UserInfo.objects.all()
    return render(request, "user/user_list.html", {"userinfo": data, "user": user})


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


@auth
def host_list(request):
    """
    主机列表
    :param request:
    :return:
    """
    user = request.session.get("name")
    return render(request, "host/host_list.html", {"user": user})


class BsLine(View):
    """
    业务线页面
    """

    @method_decorator(auth)
    def get(self, request):
        data = models.Product.objects.all()
        return render(request, "bsline/bsline_list.html", {"data": data})


class AddBsline(View):
    """
    添加业务线
    """

    @method_decorator(auth)
    def get(self, request):
        return render(request, "bsline/add_asline.html")

    def post(self, request):
        name = request.POST.get("name")
        if not models.Product.objects.filter(name=name).filter():
            models.Product.objects.create(name=name)
            return redirect("/bsline_list/")
        else:
            return render(request, "bsline/add_asline.html", {"msg": "业务名已经存在！"})


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
        bsline_id = request.GET.get("id")
        bsline_name = models.Product.objects.filter(id=bsline_id).first()
        return render(request, "bsline/edit_bsline.html", {"name": bsline_name.name})

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


def init():
    """
    初始化数据库
    :return:
    """
    password = Public.md5("admin", "123456")
    if not models.UserInfo.objects.filter(username="admin").first():
        models.UserInfo.objects.create(username="admin", password=password)


init()
