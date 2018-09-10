from django.contrib import admin
from fault_reporting import models

# 需要在Admin页面显示表，需要在这里注册
admin.site.register(models.UserInfo)
admin.site.register(models.Classify)
admin.site.register(models.Comment)
admin.site.register(models.Fault)
admin.site.register(models.Tag)
admin.site.register(models.UpDown)
admin.site.register(models.FaultDetail)
admin.site.register(models.Fault2Tag)

