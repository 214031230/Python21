from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from app01 import models
from django.urls import reverse
from django import views
from django.utils.decorators import method_decorator
from functools import wraps
# Create your views here.


# 装饰器版本登录认证
def login_check(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        next = request.path_info
        # 登录验证
        # v = request.COOKIES.get("s21")  # 取正常的cookie
        v = request.get_signed_cookie("s21", default="", salt="ooxx")  # 获取加盐的cookie
        if v == "hao":
            return func(request, *args, **kwargs)
        else:
            return redirect("/login/?next={}".format(next))
    return inner


def publisher_list(request):
    # 从请求中找有没有我之前登录时候保存的特殊的键值对
    print(request.COOKIES)
    v = request.COOKIES.get("s21")
    # 如果你请求携带的值 和我之前让你保存的是同一个，就表示你是已经登陆过的用户，默认放行
    if v == "hao":
        print(request.path_info)
        data = models.Publisher.objects.all()
        return render(request, "publisher_list.html", {"publisher_list": data})
    else:
        return redirect("/login/")


# def edit_publisher(request):
#     if request.method == "POST":
#         # 接收用户提交过来的数据
#         edit_id = request.POST.get("id")
#         new_name = request.POST.get("name888")
#         # 去数据库修改出版社名字
#         obj = models.Publisher.objects.get(id=edit_id)
#         obj.name = new_name
#         obj.save()
#         return redirect("/publisher_list/")
#     # 取url携带的参数
#     print(request.GET.get("id"))
#     edit_id = request.GET.get("id")
#     # 去数据库找编辑的出版社
#     publisher_obj = models.Publisher.objects.get(id=edit_id)
#
#     return render(request, "edit_publisher.html", {"obj": publisher_obj})


# day17课件 urls.py
# FBV
# def edit_publisher(request, edit_id):
#     print(reverse('alex'))
#     print("=" * 120)
#     if request.method == "POST":
#         new_name = request.POST.get("name888")
#         # 去数据库修改出版社名字
#         obj = models.Publisher.objects.get(id=edit_id)
#         obj.name = new_name
#         obj.save()
#         return redirect(reverse('alex'))
#     print(edit_id)
#     publisher_obj = models.Publisher.objects.get(id=edit_id)
#     return render(request, "edit_publisher.html", {"obj": publisher_obj})


# CBV
class EditPublisher(views.View):
    def get(self, request, edit_id):
        publisher_obj = models.Publisher.objects.get(id=edit_id)
        return render(request, "edit_publisher.html", {"obj": publisher_obj})

    def post(self, request, edit_id):
        new_name = request.POST.get("name888")
        # 去数据库修改出版社名字
        obj = models.Publisher.objects.get(id=edit_id)
        obj.name = new_name
        obj.save()
        return redirect(reverse('alex'))


# Django上传文件示例
class Upload(views.View):
    def get(self, request):
        return render(request, "upload.html")

    def post(self, request):
        # 拿到用户发送的文件数据
        file_obj = request.FILES.get("code")
        # 保存下来
        # 1. 拿到用户上传的文件名
        filename = file_obj.name
        # 2. 在服务端创建一个同名的文件
        with open(filename, "wb") as f:
            # 3. 从用户上传的文件对象中一点一点读数据，往我本地创建的文件句柄里一点一点写
            for i in file_obj.chunks():
                f.write(i)
        return HttpResponse("上传成功！")


# 返回JSON格式数据
class JsonTest(views.View):
    def get(self, request):
        res = {"code": 0, "data": "alex"}
        res2 = ["alex", "污Sir", "金老板", "小姨妈", "MJJ"]
        # 1. 先将字典序列化成json格式的字符串
        # import json
        # s = json.dumps(res2, ensure_ascii=False)
        # return HttpResponse(s)
        return JsonResponse(res2, safe=False)


# 测试模板语法
def template_test(request):
    data = ["金老板", "景女神", "MJJ"]
    # data = ""
    filesize = 1234567890
    import datetime
    today = datetime.datetime.today()
    link = "<script>for(;;){alert(123)}</script>"


    class Person(object):
        def __init__(self, name, dream):
            self.name = name
            self.dream = dream

        def dream(self):
            return "我的梦想是学好Python!"
    pw = Person("彭玮", "不去下一期！")

    return render(request, "t.html", {
        "data": data,
        "file_size": filesize,
        "today": today,
        "link": link,
        "person": pw
    })


def csrf_test(request):
    if request.method == "POST":
        print(request.POST)
        return HttpResponse("OK")
    return render(request, "csrf_test.html")


@login_check
def book_list(request):
    # 去数据库查询所有的书籍
    data = models.Book.objects.all()
    return render(request, "book_list.html", {"book_list": data})


class AddBook(views.View):

    @method_decorator(login_check)
    def get(self, request):
        data = models.Publisher.objects.all()
        return render(request, "add_book.html", {"publisher_list": data})

    def post(self, request):
        book_name = request.POST.get("title")
        publisher_id = request.POST.get("publisher")
        publisher_obj = models.Publisher.objects.get(id=publisher_id)
        # 创建书籍
        models.Book.objects.create(
            title=book_name,
            publisher_id=publisher_id
            # publisher=publisher_obj
        )
        return redirect("/book_list/")


class DeleteBook(views.View):
    def get(self, request, pk):
        models.Book.objects.filter(id=pk).delete()
        return redirect("/book_list/")


class EditBook(views.View):
    def get(self, request, pk):
        book_obj = models.Book.objects.get(id=pk)
        publisher_list = models.Publisher.objects.all()
        return render(request, "edit_book.html", {"book": book_obj, "publisher_list":publisher_list})

    def post(self, request, pk):
        book_obj = models.Book.objects.get(id=pk)
        new_title = request.POST.get("title")
        new_publisher_id = request.POST.get("publisher")
        # 更新
        book_obj.title = new_title
        book_obj.publisher_id = new_publisher_id
        # 同步到数据库
        book_obj.save()
        return redirect("/book_list/")


# 登录
def login(request):
    if request.method == "POST":
        next = request.GET.get("next")
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")

        if username == "alex" and pwd == "alexdsb":
            if next:
                rep = redirect(next)
            else:
                rep = redirect("/publisher_list/")
            # 在返回响应的时候 告诉浏览器保存我指定的键值对（cookie）
            # rep.set_cookie("s21", "hao", max_age=7)  # 7秒钟有效的Cookie
            rep.set_signed_cookie("s21", "hao", salt="ooxx", max_age=7)  # 设置加盐的cookie
            return rep
        else:
            return HttpResponse("滚~")

    return render(request, "login.html")
