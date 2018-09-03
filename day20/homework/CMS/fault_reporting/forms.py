#!/usr/bin/env python3
from django import forms
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import models


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ["username", "last_name", "email"]
        labels = {
            "username": "用户名",
            "last_name": "昵称",
            "email": "邮箱"
        }
        widgets = {
            "username": forms.widgets.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.widgets.TextInput(attrs={"class": "form-control"}),
            "email": forms.widgets.EmailInput(attrs={"class": "form-control"}),
        }


class RegisterModelForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ["username", "password", "last_name", "email"]
        labels = {
            "username": "用户名",
            "password": "密码",
            "last_name": "昵称",
            "email": "邮箱地址"
        }
        widgets = {
            "username": forms.widgets.TextInput(attrs={"class": "form-control", "placeholder": "用户名"}),
            "password": forms.widgets.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"}),
            "last_name": forms.widgets.TextInput(attrs={"class": "form-control", "placeholder": "昵称"}),
            "email": forms.widgets.EmailInput(attrs={"class": "form-control", "placeholder": "邮箱地址"}),
        }
