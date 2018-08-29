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
    name = models.CharField(max_length=12, verbose_name="作者名称")
    gender = models.SmallIntegerField(
        choices=((0, "女"), (1, "男"), (2, "保密")),
        default=2,
        verbose_name="性别"
    )
    age = models.IntegerField(verbose_name="年龄")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "作者管理"
        verbose_name_plural = verbose_name


class Book(models.Model):
    title = models.CharField(max_length=32, unique=True, verbose_name="书籍名称")
    # auto_now_add:创建时间  auto_add:修改时间
    publish_date = models.DateField(auto_now_add=True, verbose_name="出版时间")
    phone = models.CharField(max_length=11, unique=True, null=True, blank=True, verbose_name="手机号")
    publisher = models.ForeignKey(to="Publisher", on_delete=models.CASCADE, verbose_name="出版社")
    authors = models.ManyToManyField(to="Author", verbose_name="作者")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "书籍管理"
        verbose_name_plural = verbose_name
