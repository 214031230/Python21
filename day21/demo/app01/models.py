from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=16, verbose_name="图书名称")

    class Meta:
        verbose_name = "图书表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
