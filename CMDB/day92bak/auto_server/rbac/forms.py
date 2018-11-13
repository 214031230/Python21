#!/usr/bin/env python3
from django import forms
from rbac import models


class MenusModelForm(forms.ModelForm):
    class Meta:
        model = models.Menu
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(MenusModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class RolesModelForm(forms.ModelForm):
    class Meta:
        model = models.Role
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(RolesModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class PermissionModelForm(forms.ModelForm):
    class Meta:
        model = models.Permission
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PermissionModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

