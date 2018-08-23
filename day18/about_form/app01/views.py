from django.shortcuts import render, HttpResponse
from django import forms
from django.forms import widgets
from app01 import models


# Create your views here.
class RegisterForm(forms.Form):
    user = forms.CharField(min_length=6, max_length=8,
                           label="用户名", widget=widgets.TextInput(attrs={"class": "form-control", "placeholder": "用户名"}),
                           error_messages={"min_length": "*用户名长度不能少6位",
                                           "required": "*必填项"})
    pwd = forms.CharField(min_length=6, max_length=8,
                          label="密码",
                          widget=widgets.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"}),
                          error_messages={"min_length": "*密码长度不能少6位",
                                          "required": "*必填项"})


def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            models.User.objects.create(user=request.POST.get("user"), pwd=request.POST.get("pwd"))
            return HttpResponse("注册成功")
        else:
            return render(request, "register.html", locals())
    register_form = RegisterForm()
    return render(request, "register.html", locals())
