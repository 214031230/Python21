from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
# Create your views here.


# 自定义一个字段的校验规则函数
def phone_validate(value):
    # 拿用户填写的手机号去数据库查找有没有
    is_exist = models.Book.objects.filter(phone=value)
    if is_exist:
        # 如果该手机号已经被使用就不能再注册
        raise ValidationError("该手机号已经被注册！")
    else:
        return value


# 自定义一个form类
class BookForm(forms.Form):
    title = forms.CharField(
        max_length=12,
        min_length=6,
        label="书名",
        # initial="书名的默认值",
        widget=forms.widgets.TextInput(attrs={"class": "form-control"})
    )
    publish_date = forms.DateField(
        label="出版日期",
        widget=forms.widgets.DateInput(attrs={"type": "date", "class": "form-control"})
    )
    phone = forms.CharField(
        max_length=11,
        # required=False,
        # validators=[RegexValidator(r'^1[356789]\d{9}$', "手机号码格式不正确"), phone_validate],
        validators=[RegexValidator(r'^1[356789]\d{9}$', "手机号码格式不正确")],
        widget=forms.widgets.TextInput(attrs={"class": "form-control"})
    )
    # publisher = forms.ChoiceField(
    #     # choices=models.Publisher.objects.values_list("id", "name"),
    #     widget=forms.widgets.Select()
    # )
    publisher = forms.ModelChoiceField(
        queryset=models.Publisher.objects.all(),
        widget=forms.widgets.Select(attrs={"class": "form-control"})
    )
    authors = forms.ModelMultipleChoiceField(
        queryset=models.Author.objects.all(),
        widget=forms.widgets.SelectMultiple(attrs={"class": "form-control"})
    )

    # 自定义一个局部钩子函数
    def clean_title(self):
        value = self.cleaned_data.get("title")
        # 判断有没有敏感词
        if "alex" in value:
            raise ValidationError("alex已被河蟹...")
        else:
            return value

    # 全局钩子函数
    def clean(self):
        # 可以从self.cleaned_data取到所有字段的数据
        # self.add_error("字段", "密码和确认密码不一致")
        pass


def book_list(request):
    data = models.Book.objects.all()
    # return render(request, "book_list.html", {"data": data})
    # locals()以字典的形式把当前作用域的变量表示出来
    return render(request, "book_list.html", locals())


def add_book(request):
    form_obj = BookForm()
    if request.method == "POST":
        # 从用户提交过来的数据中取数据
        # 做校验
        form_obj = BookForm(request.POST)
        if form_obj.is_valid():  # 做数据有效性的校验
            # 去数据库创建新的数据
            print(form_obj.cleaned_data)
            # 因为有多对多的字段，所以需要额外处理
            authors = form_obj.cleaned_data.pop("authors")
            # 创建新书籍对象
            book_obj = models.Book.objects.create(**form_obj.cleaned_data)
            # 将书籍对象和作者建立关联
            book_obj.authors.add(*authors)
            return redirect("/book_list/")

    return render(request, "add_book.html", locals())


def edit_book(request, pk):
    book_obj = models.Book.objects.filter(id=pk).first()
    # book_dict = {
    #     "title": book_obj.title,
    #     "publish_date": book_obj.publish_date.strftime("%Y-%m-%d"),
    # }
    # 把ORM中一个对象 快速转换成 字典格式
    from django.forms import model_to_dict
    book_dict = model_to_dict(book_obj)
    book_dict["publish_date"] = book_obj.publish_date.strftime("%Y-%m-%d")
    print(book_dict)
    print("=" * 120)
    # form_obj = BookForm({"title": "书的默认值呀2", "publish_date": "2018-01-01"})
    form_obj = BookForm(book_dict)
    if request.method == "POST":
        # 从用户提交过来的数据中取数据
        form_obj = BookForm(request.POST)
        if form_obj.is_valid():
            # 去数据库更新对应的书籍
            book_obj.title = form_obj.cleaned_data.get("title")
            book_obj.publish_date = form_obj.cleaned_data.get("publish_date")
            book_obj.publisher_id = form_obj.cleaned_data.get("publisher")
            book_obj.save()
            book_obj.authors.set(form_obj.cleaned_data.get("authors"))  # 让ORM去更新第三张关系表
            return redirect("/book_list/")

    return render(request, "edit_book.html", locals())
