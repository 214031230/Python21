from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserInfo(AbstractUser):
    """
    用户表，
        新增手机号字段
        新增头像字段
    """
    phone = models.CharField(max_length=11, verbose_name="手机号")
    avatar = models.FileField(upload_to="avatars", default="avatars/default.png", verbose_name="头像")

    class Meta:
        verbose_name = "用户管理"
        verbose_name_plural = verbose_name


class Fault(models.Model):
    """
    故障表
    """
    title = models.CharField(max_length=50, verbose_name="故障标题")
    summary = models.TextField(max_length=100, verbose_name="故障概述")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    modify_time = models.DateTimeField(auto_now=True, verbose_name="最后修改时间")
    tags = models.ManyToManyField(to="Tag",
                                  through="Fault2Tag",  # 指定第三张关系表
                                  through_fields=("fault", "tag"),  # 通过哪些字段建立多对多关系
                                  verbose_name="标签")
    classify = models.ForeignKey(to="Classify", verbose_name="分类", null=True)
    user = models.ForeignKey(to="UserInfo", verbose_name="发布用户")

    comment_count = models.IntegerField(default=0, verbose_name="评论总数")
    up_count = models.IntegerField(default=0, verbose_name="点赞总数")
    down_count = models.IntegerField(default=0, verbose_name="反正总数")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "故障管理"
        verbose_name_plural = verbose_name


class Tag(models.Model):
    """
    标签表
    """
    name = models.CharField(max_length=30, verbose_name="标签名称", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签管理"
        verbose_name_plural = verbose_name


class Classify(models.Model):
    """
    分类表
    """
    name = models.CharField(max_length=30, verbose_name="业务线名称", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "业务线管理"
        verbose_name_plural = verbose_name


class Comment(models.Model):
    """
    评论表
    """
    content = models.CharField(max_length=100, verbose_name="评论内容")
    comment_date = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
    fault = models.ForeignKey(to="Fault", verbose_name="故障总结")
    user = models.ForeignKey(to="UserInfo", verbose_name="评论用户")
    parent_comment = models.ForeignKey(to="self", null=True, blank=True, verbose_name="父级评论")  # 自己关联自己，用户可以评论其他人的评论

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "评论管理"
        verbose_name_plural = verbose_name


class UpDown(models.Model):
    """
    点赞表
    同一个用户只能对一篇文章进行点赞或者反对，如果点赞了就不能反对，二选一
    """
    user = models.ForeignKey(to="UserInfo", verbose_name="用户")
    fault = models.ForeignKey(to="Fault", verbose_name="故障总结")
    is_up = models.BooleanField(default=True, verbose_name="支持/反对")

    def __str__(self):
        return "{}-{}-{}".format(self.user.username, self.fault.title, "支持" if self.is_up else "反对")

    class Meta:
        """
        unique_together联合唯一，限制一用户只能对一篇文章进行点赞或者反对
        """
        unique_together = (("user", "fault"),)
        verbose_name = "支持/反对"
        verbose_name_plural = verbose_name


class Fault2Tag(models.Model):
    """
    故障报告和标签多对多关联表
    """
    fault = models.ForeignKey(to="Fault", verbose_name="故障总结")
    tag = models.ForeignKey(to="Tag", verbose_name="标签名称")

    def __str__(self):
        return "{}-{}".format(self.fault.title, self.tag.name)

    class Meta:
        unique_together = (("fault", "tag"),)
        verbose_name = "故障-标签"
        verbose_name_plural = verbose_name


class FaultDetail(models.Model):
    """
    故障内容表
    为什么不和故障表放到一起?
        故障内容可能多，用户每次请求页面的时候都请求故障内容，就会很慢。
    """
    content = models.TextField(verbose_name="故障内容")
    fault = models.ForeignKey(to="Fault", verbose_name="故障总结")

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "故障详情"
        verbose_name_plural = verbose_name
