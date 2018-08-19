from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from django import views
# Create your views here.


def author_list(request):
    author_list = models.Author.objects.all()
    return render(request, "author_list.html", {"data": author_list})


def delete_author(request, delete_id):
    # models.Author.objects.get(id=delete_id)  # 很少用，谨慎使用
    models.Author.objects.filter(id=delete_id).delete()
    return redirect("/author_list/")


# 添加作者
class AddAuthor(views.View):

    def get(self, request):
        book_list = models.Book.objects.all()
        return render(request, "add_author.html", {"book_list": book_list})

    def post(self, request):
        print(request.POST)
        # 用户新创建的作者名字
        author_name = request.POST.get("name")
        # 用户给新作者设置的书名id, 因为是多选所以要用getlist取值
        books_ids = request.POST.getlist("books")
        print(author_name, books_ids)
        # 1. 先创建一个新的作者对象
        author_obj = models.Author.objects.create(name=author_name)
        # 2. 去第三张关系表，建立关系记录
        author_obj.books.set(books_ids)
        return redirect("/author_list/")
        # return HttpResponse("OK")


class EditAuthor(views.View):
    def get(self, request, edit_id):
        author_obj = models.Author.objects.filter(id=edit_id).first()
        book_list = models.Book.objects.all()
        return render(request, "edit_author.html", {"author": author_obj, "book_list": book_list})


    def post(self, request, edit_id):
        author_obj = models.Author.objects.filter(id=edit_id).first()

        new_name = request.POST.get("name")
        new_books = request.POST.getlist("books")

        # 真正的更新操作
        author_obj.name = new_name
        author_obj.save()

        author_obj.books.set(new_books)
        return redirect("/author_list/")



