from django import forms

from crm import models


class DepartModelForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = '__all__'
        error_messages = {
            'title': {'required': '部门名称不能为空'}
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }
