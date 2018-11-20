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
            

class BusinessUnitModelForm(ModelForm):
    class Meta:
        model = models.BusinessUnit
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BusinessUnitModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class IdcModelForm(ModelForm):
    class Meta:
        model = models.IDC
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(IdcModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class ServerModelForm(ModelForm):
    class Meta:
        model = models.Server
        exclude = ["create_at", "latest_date"]

    def __init__(self, *args, **kwargs):
        super(ServerModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
            
            
class TagModelForm(ModelForm):
    class Meta:
        model = models.Tag
        exclude = ["create_at", "latest_date"]

    def __init__(self, *args, **kwargs):
        super(TagModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class DiskModelForm(ModelForm):
    class Meta:
        model = models.Disk
        exclude = ["create_at", "latest_date"]

    def __init__(self, *args, **kwargs):
        super(DiskModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class NicModelForm(ModelForm):
    class Meta:
        model = models.NIC
        exclude = ["create_at", "latest_date"]

    def __init__(self, *args, **kwargs):
        super(NicModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class MemoryModelForm(ModelForm):
    class Meta:
        model = models.Memory
        exclude = ["create_at", "latest_date"]

    def __init__(self, *args, **kwargs):
        super(MemoryModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class ServerRecordModelForm(ModelForm):
    class Meta:
        model = models.ServerRecord
        exclude = ["create_at", "latest_date"]

    def __init__(self, *args, **kwargs):
        super(ServerRecordModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"