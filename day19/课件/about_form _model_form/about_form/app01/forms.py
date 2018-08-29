from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app01 import models


# 写一个和Model类一一对应的form
class BookModelForm(forms.ModelForm):
    class Meta:
        model = models.Book
        # fields = "__all__"  # model类里所有的字段都展示
        # fields = ["title", ]  # 指定展示某些字段
        exclude = ["title", ]  # 除了指定字段，其他字段都展示
        labels = {  # 设置label标签名
            "title": "书名",
            "phone": "手机号",
            "publisher": "出版社",
            "authors": "作者",
        }
        widgets = {  # 设置每个字段的插件信息
            "title": forms.widgets.TextInput(attrs={"class": "form-control"}),
            "phone": forms.widgets.TextInput(attrs={"class": "form-control"}),
            "publisher": forms.widgets.Select(attrs={"class": "form-control"}),
            "authors": forms.widgets.SelectMultiple(attrs={"class": "form-control"}),
        }
        error_messages = {  # 设置每个字段的报错提示信息
            "publisher": {
                "required": "必须给我选一个出版社！"
            }
        }
