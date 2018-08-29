from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from app01.forms import BookForm, BookModelForm
# Create your views here.


def book_list(request):
    data = models.Book.objects.all()
    # return render(request, "book_list.html", {"data": data})
    # locals()以字典的形式把当前作用域的变量表示出来
    return render(request, "book_list.html", locals())


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
