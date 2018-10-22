#!/usr/bin/env python3
from django import forms
from api import models


# 写一个和Model类一一对应的form
class ApplicationModelForm(forms.ModelForm):
    class Meta:
        model = models.Application
        fields = "__all__"  # model类里所有的字段都展示
        labels = {  # 设置label标签名
            "title": "应用名称",
        }
        widgets = {  # 设置每个字段的插件信息
            "title": forms.widgets.TextInput(attrs={"class": "form-control"}),
        }
        error_messages = {  # 设置每个字段的报错提示信息
            "title": {
                "required": "应用名称必填！"
            }
        }


class ApiModelForm(forms.ModelForm):
    class Meta:
        model = models.Api
        fields = "__all__"  # model类里所有的字段都展示
        labels = {  # 设置label标签名
            "url": "Api_url",
            "app": "所属应用",
        }
        widgets = {  # 设置每个字段的插件信息
            "url": forms.widgets.TextInput(attrs={"class": "form-control"}),
            "app": forms.widgets.TextInput(attrs={"class": "form-control"}),
        }
        error_messages = {  # 设置每个字段的报错提示信息
            "url": {
                "required": "Api地址必填！"
            },
            "app": {
                "required": "必须选则所属应用！"
            }
        }
