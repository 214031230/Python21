from django.db import models


class UserInfo(models.Model):
    """
    创建用户表
    """
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=64)


class Product(models.Model):
    """
    创建业务产品表
    """
    name = models.CharField(max_length=32, unique=True)
    # create_date = models.DateTimeField(auto_now_add=True)
    # update_date = models.DateTimeField(auto_now=True)


class HostInfo(models.Model):
    """
    创建主机表
    """
    ip = models.CharField(max_length=11, unique=True)
    hostname = models.CharField(max_length=32, unique=True, default="localhost")
    product = models.ForeignKey(to="Product")
    # create_date = models.DateTimeField(auto_now_add=True)
    # update_date = models.DateTimeField(auto_now=True)
