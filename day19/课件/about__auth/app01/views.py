from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from app01.forms import BookForm, BookModelForm
from django import views
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def book_list(request):
    data = models.Book.objects.all()
    return render(request, "book_list.html", locals())


@login_required
def add_book(request):
    form_obj = BookModelForm()
    if request.method == "POST":
        # 从用户提交过来的数据中取数据
        # 做校验
        form_obj = BookModelForm(request.POST)
        if form_obj.is_valid():  # 做数据有效性的校验
            form_obj.save()
            return redirect("/book_list/")
    return render(request, "add_book.html", locals())


def edit_book(request, pk):
    book_obj = models.Book.objects.filter(id=pk).first()
    form_obj = BookModelForm(instance=book_obj)
    if request.method == "POST":
        # 从用户提交过来的数据中取数据
        form_obj = BookModelForm(request.POST, instance=book_obj)
        if form_obj.is_valid():
            # 去数据库更新对应的书籍
            form_obj.save()
            return redirect("/book_list/")
    return render(request, "edit_book.html", locals())


class LoginView(views.View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        next_url = request.GET.get("next")
        print(request.POST)
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        user_obj = auth.authenticate(request, username=username, password=pwd)
        if user_obj:
            # 用户名和密码正确
            auth.login(request, user_obj)  # 给该次请求设置了session数据，并在响应中回写cookie
            if next_url:
                return redirect(next_url)
            else:
                return redirect("/book_list/")
        else:
            # 用户名或密码错误
            return render(request, "login.html", {"error_msg": "用户名或密码错误"})


class RegView(views.View):
    def get(self, request):
        return render(request, "reg.html")

    def post(self, request):
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        # 去数据库中创建用户
        # User.objects.create()  --> 直接在数据库创建用户，密码是存的明文的
        user_obj = User.objects.create_user(username=username, password=pwd)
        # User.objects.create_superuser()
        return redirect("/login/")
