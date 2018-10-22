from django.contrib import admin
from rbac import models

admin.site.register(models.Menu)
# admin.site.register(models.Permission)
admin.site.register(models.Role)
admin.site.register(models.UserInfo)


# # 自定义一个权限的管理类
class PermissionAdmin(admin.ModelAdmin):
    # 告诉Django admin在页面上展示我这张表的哪些字段
    list_display = ["id", "url", "title", "name", "menu", "parent"]
    # 在列表页面支持直接修改的字段
    # list_editable 第一个索引不能为list_display的第一个索引否则会报错：
    list_editable = ["url", "title", "name", "menu", "parent"]


admin.site.register(models.Permission, PermissionAdmin)
