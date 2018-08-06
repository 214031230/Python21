from django.db import models


class UserInfo(models.Model):
    """
    创建用户表
    """
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=64)
