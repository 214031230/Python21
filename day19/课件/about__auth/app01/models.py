from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name="出版社名称")
    address = models.TextField(verbose_name="出版社地址")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "出版社"
        verbose_name_plural = verbose_name


class Author(models.Model):
    name = models.CharField(max_length=12)
    gender = models.SmallIntegerField(
        choices=((0, "女"), (1, "男"), (2, "保密")),
        default=2
    )
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=32, unique=True)
    # auto_now_add:创建时间  auto_add:修改时间
    publish_date = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=11, unique=True, null=True, blank=True)
    publisher = models.ForeignKey(to="Publisher", on_delete=models.CASCADE)
    authors = models.ManyToManyField(to="Author")

    def __str__(self):
        return self.title


from django.contrib.auth.models import AbstractUser
# 扩展默认的auth_user表

#
# class UserInfo(AbstractUser):
#     phone = models.CharField(max_length=11)
