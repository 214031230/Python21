from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app01 import models


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
    # authors = forms.ChoiceField(
    #     choices=models.Author.objects.values_list("id", "name"),
    #     widget=forms.widgets.SelectMultiple()
    # )
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