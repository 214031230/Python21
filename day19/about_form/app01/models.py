from django.db import models


# Create your models here.


class Book(models.Model):
    """
    书籍表
    """
    name = models.CharField(max_length=36, verbose_name="图书", unique=True)
    publisher = models.ForeignKey(to="Publisher", default=None, verbose_name="出版社")
    authors = models.ManyToManyField(to="Author", verbose_name="作者")
    create_time = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "图书管理"
        verbose_name_plural = verbose_name


class Publisher(models.Model):
    """
    出版社表
    """
    name = models.CharField(max_length=36, verbose_name="出版社", unique=True)
    address = models.TextField(verbose_name="出版社地址")
    create_time = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "出版社管理"
        verbose_name_plural = verbose_name


class Author(models.Model):
    """
    作者表
    """
    name = models.CharField(max_length=12, verbose_name="作者")
    sex = models.SmallIntegerField(
        choices=((0, "女"), (1, "男"), (2, "保密")),
        default=2,
        verbose_name="性别"
    )
    age = models.IntegerField(verbose_name="年龄", null=True)
    create_time = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "作者管理"
        verbose_name_plural = verbose_name
