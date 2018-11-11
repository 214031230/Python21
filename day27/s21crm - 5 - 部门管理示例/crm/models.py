from django.db import models
from rbac.models import AbstractUserInfo


class Department(models.Model):
    """
    部门表
    """
    title = models.CharField(verbose_name='部门', max_length=32)


class UserInfo(AbstractUserInfo):
    """
    用户表
    """

    gender_choice = (
        (1, "男"),
        (0, "女")
    )
    gender = models.IntegerField(verbose_name="性别", choices=gender_choice, default=1)
    depart = models.ForeignKey(verbose_name='部门', to='Department')
    
    email = models.EmailField(verbose_name='邮箱')
    phone = models.CharField(verbose_name='手机', max_length=32)
