from django.shortcuts import render, redirect
from app01 import models


# Create your views here.

def book_list(request):
    """
    书籍列表
    :param request:
    :return:
    """
    data = models.Book.objects.all()
    return render(request, "book_list.html", locals())


def add_book(request):
    """
    添加书籍
    :param request:
    :return:
    """

    if request.method == "POST":
        book_name = request.POST.get("book_name")
        publisher_name = request.POST.get("publisher_name")
        author_name = request.POST.getlist("author_name")
        book_obj = models.Book.objects.create(name=book_name, publisher_id=publisher_name)
        book_obj.authors.add(*author_name)
        return redirect("/book_list/")
    authors = models.Author.objects.all()
    publishers = models.Publisher.objects.all()
    return render(request, "add_book.html", locals())


def edit_book(request, book_id):
    """
    编辑书籍
    :param request:
    :return:
    """
    book_obj = models.Book.objects.filter(id=book_id).first()
    if request.method == "POST":
        book_name = request.POST.get("book_name")
        publisher_name = request.POST.get("publisher_name")
        author_name = request.POST.getlist("author_name")
        book_obj.name = book_name
        book_obj.publisher_id = publisher_name
        book_obj.save()
        book_obj.authors.set(author_name)
        return redirect("/book_list/")

    authors = models.Author.objects.all()
    publishers = models.Publisher.objects.all()
    return render(request, "edit_book.html", locals())
