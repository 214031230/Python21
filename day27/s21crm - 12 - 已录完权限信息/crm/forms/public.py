from django import forms
from crm import models


class PublicCustomerModelForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        # fields = "__all__"
        # fields = ['name','qq']
        exclude = ['consultant','status']
        
    def __init__(self, *args, **kwargs):
        # 在父类的初始化方法中将7个字段当成字典放到了 self.fields 中。
        super(PublicCustomerModelForm, self).__init__(*args, **kwargs)
        
        for key, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    