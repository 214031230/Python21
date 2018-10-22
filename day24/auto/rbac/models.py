from django.db import models

# Create your models here.

"""
权限系统包含6张表
1. 用户表
2. 角色表
3. 用户角色关系表 （用户和角色是多对多的关系）
4. 权限表
5. 权限角色关系表 （权限和角色是多对多的关系）
6. 菜单表（菜单和权限是一对多的关系）
"""


class Menus(models.Model):
    """
    菜单表
    """
    title = models.CharField(max_length=32, verbose_name="名称")
    icon = models.CharField(max_length=32, verbose_name="图标")


class Permission(models.Model):
    """
    权限表
    """
    url = models.CharField(max_length=125, verbose_name="URL路径")
    title = models.CharField(max_length=32, verbose_name="URL名称")
    name = models.CharField(max_length=36, verbose_name="别名", unique=True)
    menu = models.ForeignKey(to="Menus", verbose_name="关联菜单", null=True, blank=True)
    parent = models.ForeignKey(to="Permission", verbose_name="父级菜单", null=True, blank=True)


class Role(models.Model):
    """
    角色表
    """
    name = models.CharField(max_length=32, verbose_name="名称")
    permissions = models.ManyToManyField(to="Permission", verbose_name="关联权限")


class UserInfo(models.Model):
    """
    用户表
    """
    name = models.CharField(max_length=32, verbose_name="用户名")
    password = models.CharField(max_length=128, verbose_name="密码")
    roles = models.ManyToManyField(to="Role", verbose_name="角色ID")
