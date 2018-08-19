from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=12)


# 书籍表
class Book(models.Model):
    title = models.CharField(max_length=32)
    publisher = models.ForeignKey(to="Publisher", on_delete=models.CASCADE)


# 作者表
class Author(models.Model):
    name = models.CharField(max_length=12)
    # 多对多,自动帮我们在数据库建立第三张关系表
    books = models.ManyToManyField(to='Book', related_name="authors")


