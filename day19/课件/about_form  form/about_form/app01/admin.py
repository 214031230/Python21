from django.contrib import admin
from app01 import models
# Register your models here.


# 将app中的表 注册到admin中，注册之后就能在admin页面对表做管理
admin.site.register(models.Publisher)
admin.site.register(models.Author)
admin.site.register(models.Book)

