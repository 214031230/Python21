#!/usr/bin/env python3
from django import forms
from fault_reporting import models


class UserModelForm(forms.ModelForm):
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


class RegisterModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["username", "password", "last_name", "phone", "email"]
        labels = {
            "username": "用户名",
            "password": "密码",
            "last_name": "昵称",
            "phone": "手机号",
            "email": "邮箱地址"
        }
        widgets = {
            "username": forms.widgets.TextInput(attrs={"class": "form-control", "placeholder": "用户名"}),
            "password": forms.widgets.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"}),
            "last_name": forms.widgets.TextInput(attrs={"class": "form-control", "placeholder": "昵称"}),
            "phone": forms.widgets.TextInput(attrs={"class": "form-control", "placeholder": "手机号"}),
            "email": forms.widgets.EmailInput(attrs={"class": "form-control", "placeholder": "邮箱地址"}),
        }
