from django.forms import ModelForm
from repository import models


class UserProfileModelForm(ModelForm):
    class Meta:
        model = models.UserProfile
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(UserProfileModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class AdminInfoModelForm(ModelForm):
    class Meta:
        model = models.AdminInfo
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(AdminInfoModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class UserGroupModelForm(ModelForm):
    class Meta:
        model = models.UserGroup
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(UserGroupModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
