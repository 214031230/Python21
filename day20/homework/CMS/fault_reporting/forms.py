#!/usr/bin/env python3
from django import forms
from fault_reporting import models
from django.core.validators import RegexValidator  # form 正则校验
from django.core.exceptions import ValidationError  # 抛出异常


class UserModelForm(forms.ModelForm):
    """
    用户登录校验，使用modelform
    labels 在页面显示的字段名称
    fields 显示指定字段 这里必须和数据库字段对应
    widgets input框的样式和属性  form-control 是bootstrap样式类(前端页面是循环生成的input框无法在添加增加样式)
    model
    """

    class Meta:
        model = models.UserInfo
        fields = ["username", "last_name", "phone", "email"]
        labels = {
            "username": "用户名",
            "last_name": "昵称",
            "phone": "手机号",
            "email": "邮箱"
        }
        widgets = {
            "username": forms.widgets.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.widgets.TextInput(attrs={"class": "form-control"}),
            "phone": forms.widgets.TextInput(attrs={"class": "form-control"}),
            "email": forms.widgets.EmailInput(attrs={"class": "form-control"}),
        }


class RegisterForm(forms.Form):
    """
    用户注册校验 使用form组件
    字段名称必须和数据库对应 re_password在数据库不存在，在存储数据前会删掉
    """
    username = forms.CharField(min_length=6,
                               label="用户名")
    password = forms.CharField(min_length=6,
                               label="密码",
                               widget=forms.widgets.PasswordInput())
    re_password = forms.CharField(min_length=6,
                                  label="确认密码",
                                  widget=forms.widgets.PasswordInput())
    phone = forms.CharField(max_length=11,
                            min_length=11,
                            validators=[RegexValidator(r"^1[3-8]\d{9}$", "手机号格式不正确")],
                            label="手机号")
    email = forms.EmailField(label="邮箱",
                             validators=[RegexValidator(
                                 r"^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$", "邮箱格式不正确")])

    def clean_username(self):
        """
        局部钩子
        检测用户名唯一性
        :return:
        """
        username = self.cleaned_data.get("username")
        is_exist = models.UserInfo.objects.filter(username=username)
        if is_exist.exists():
            raise ValidationError("用户名已经存在")
        else:
            return username

    def clean(self):
        """
        全局钩子
        检测两次输入的密码是否一致
        :return:
        """
        pwd = self.cleaned_data.get("password")
        re_pwd = self.cleaned_data.get("re_password")
        if pwd == re_pwd:
            return self.cleaned_data
        else:
            self.add_error("re_password", "两次密码输入的不一致")
            raise ValidationError("两次输入的密码不一致")

    def __init__(self, *args, **kwargs):
        """
        循环给所有的标签添加样式
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                "class": "form-control"
            })


class UserUpdate(forms.Form):
    """
    用户编辑校验
    """
    username = forms.CharField(min_length=6,
                               label="用户名",
                               widget=forms.TextInput(attrs={"readonly": "readonly"}))
    phone = forms.CharField(max_length=11,
                            min_length=11,
                            validators=[RegexValidator(r"^1[3-8]\d{9}$", "手机号格式不正确")],
                            label="手机号")
    email = forms.EmailField(label="邮箱",
                             validators=[RegexValidator(
                                 r"^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$", "邮箱格式不正确")])

    def __init__(self, *args, **kwargs):
        """
        循环给所有的标签添加样式
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                "class": "form-control"
            })
