from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from functools import wraps


def auth(func):
    @wraps(func)  # 使用wraps装饰
    def inner(request, *args, **kwargs):
        if request.get_signed_cookie("cookie", salt="spf", default="") == "123456":
            return func(request, *args, **kwargs)
        else:
            path = request.path_info # 获取用户请求路径
            return redirect("/login/?path=%s" % path) # 拼接用户请求路径到浏览器

    return inner


class Upload(View):
    """
    上传文件
    """

    @method_decorator(auth)
    def get(self, request):
        print(self.__doc__)
        return render(request, "upload.html")

    def post(self, request):
        file_obj = request.FILES.get("code")
        file_name = file_obj.name
        with open(file_name, "wb") as f:
            for i in file_obj.chunks():
                f.write(i)
        return render(request, "upload.html", {"status": "上传成功"})


class Login(View):
    """
    用户登录
    """

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        path = request.GET.get("path")
        if username == "spf" and password == "123":
            if path:  # 判断用户是否是从其他页面跳转过来的，如果是则跳转到之前页面
                obj = redirect(path)
            else:
                obj = redirect("/upload/")  # 如果不是则跳转到默认页面
            obj.set_signed_cookie("cookie", "123456", salt="spf")
            return obj
        else:
            return redirect("/login/?path=%s" % path)  # 如果登录失败则返回当前页面
