from django.shortcuts import render, redirect
from app01 import models
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


# Create your views here.
class BookForm(forms.Form):
    name = forms.CharField(max_length=12,
                           min_length=6,
                           label="书籍名称",
                           widget=forms.widgets.TextInput(attrs={"class": "form-control"}))
    phone = forms.CharField(max_length=11,
                            min_length=11,
                            label="手机号",
                            validators=[RegexValidator(r"^1[8]\d{9}$", "手机号格式不正确")],
                            widget=forms.widgets.TextInput(attrs={"class": "form-control"}))
    publisher = forms.ModelChoiceField(queryset=models.Publisher.objects.all(),
                                       label="出版社",
                                       widget=forms.widgets.Select(attrs={"class": "form-control"}))
    authors = forms.ModelMultipleChoiceField(queryset=models.Author.objects.all(),
                                             label="作者",
                                             widget=forms.widgets.SelectMultiple(attrs={"class": "form-control"}))

    # def clean_phone(self):
    #     val = self.cleaned_data.get("phone")
    #     obj = models.Book.objects.filter(phone=val)
    #     if obj.exists():
    #         raise ValidationError("手机号已经存在")
    #     else:
    #         return val
    def clean_phone(self):
        val1 = self.cleaned_data.get("name")
        val2 = self.cleaned_data.get("phone")
        if val1 != val2:
            raise ValidationError("密码不一致")


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
    form_obj = BookForm()
    if request.method == "POST":
        form_obj = BookForm(request.POST)
        if form_obj.is_valid():
            authors = form_obj.cleaned_data.pop("authors")
            book_obj = models.Book.objects.create(**form_obj.cleaned_data)
            book_obj.authors.add(*authors)
            return redirect("/book_list/")

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
