from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=12)


# 书籍表
class Book(models.Model):
    title = models.CharField(max_length=32)
    publisher = models.ForeignKey(to="Publisher", on_delete=models.CASCADE)


class Person(models.Model):
    name = models.CharField(max_length=12, default="alex")
    age = models.IntegerField(default=18)
    birthday = models.DateField()
    birthday2 = models.DateTimeField(null=True)
    phone = models.CharField(max_length=11, unique=True)
    # 创建该记录时自动把当前时间保存到该字段
    join_date = models.DateField(auto_now_add=True)
    # 更新该记录的值时 自动把当前时间保存到该字段
    last_date = models.DateField(auto_now=True)

    def __str__(self):
        return "{}-{}".format(self.age, self.phone)
