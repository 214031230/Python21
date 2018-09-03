from django.contrib import admin
from fault_reporting import models

admin.site.register(models.UserInfo)
admin.site.register(models.Classify)
admin.site.register(models.Comment)
admin.site.register(models.Fault)
admin.site.register(models.Tag)
