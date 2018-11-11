from django import forms

from crm import models


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserModelForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

