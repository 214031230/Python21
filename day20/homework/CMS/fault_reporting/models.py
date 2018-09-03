from django.db import models
from django.contrib.auth.models import  AbstractUser

# Create your models here.


# class UserInfo(AbstractUser):
#     """
#     用户表，新增手机号字段
#     """
#     phone = models.CharField(max_length=11, verbose_name="手机号")
# 
#     class Meta:
#         verbose_name = "用户"
#         verbose_name_plural = verbose_name


class Fault(models.Model):
    """
    故障表
    """
    title = models.CharField(max_length=50, verbose_name="故障标题")
    summary = models.CharField(max_length=100, verbose_name="故障概述")
    content = models.CharField(max_length=500, verbose_name="故障内容")
    create_time = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(to="Tag", verbose_name="标签")
    classify = models.ForeignKey(to="Classify", verbose_name="分类")
    user = models.ForeignKey(to="User", verbose_name="所属用户")


class Tag(models.Model):
    """
    标签表
    """
    name = models.CharField(max_length=30, verbose_name="故障标签")


class Classify(models.Model):
    """
    分类表
    """
    name = models.CharField(max_length=30, verbose_name="故障分类")


class Comment(models.Model):
    """
    评论表
    """
    fault = models.ForeignKey(to="Fault", verbose_name="报障内容")
    user = models.ForeignKey(to="User", verbose_name="评论用户")