from django.shortcuts import render, redirect
from app01 import models
from django import forms
# Create your views here.


# 自定义一个form类
class BookForm(forms.Form):
    title = forms.CharField(max_length=12)
    publish_date = forms.DateField()
    phone = forms.CharField(max_length=11)
    publisher = forms.ChoiceField()
    authors = forms.ChoiceField()


def book_list(request):
    data = models.Book.objects.all()
    # return render(request, "book_list.html", {"data": data})
    # locals()以字典的形式把当前作用域的变量表示出来
    return render(request, "book_list.html", locals())


def add_book(request):
    if request.method == "POST":
        # 从用户提交过来的数据中取数据
        title = request.POST.get("title")
        publish_date = request.POST.get("publish_date")
        phone = request.POST.get("phone")
        publisher = request.POST.get("publisher")
        authors = request.POST.getlist("authors")

        # 去数据库创建书籍
        book_obj = models.Book.objects.create(
            title=title,
            publish_date=publish_date,
            publisher_id=publisher,
        )
        book_obj.authors.add(*authors)  # add接收一个一个的值，直接传列表不行需要打散
        return redirect("/book_list/")

    publisher_list = models.Publisher.objects.all()
    author_list = models.Author.objects.all()
    return render(request, "add_book.html", locals())


def edit_book(request, pk):
    book_obj = models.Book.objects.filter(id=pk).first()
    if request.method == "POST":
        # 从用户提交过来的数据中取数据
        title = request.POST.get("title")
        publish_date = request.POST.get("publish_date")
        publisher = request.POST.get("publisher")
        authors = request.POST.getlist("authors")
        # 去数据库更新对应的书籍
        book_obj.title = title
        book_obj.publish_date = publish_date
        book_obj.publisher_id = publisher
        book_obj.save()
        book_obj.authors.set(authors)  # 让ORM去更新第三张关系表
        return redirect("/book_list/")

    publisher_list = models.Publisher.objects.all()
    author_list = models.Author.objects.all()
    return render(request, "edit_book.html", locals())
