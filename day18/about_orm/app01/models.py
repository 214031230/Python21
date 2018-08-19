from django.db import models


# Create your models here.
class Publisher(models.Model):
    """
    出版社表
    """
    name = models.CharField(max_length=24)


class Book(models.Model):
    """
    图书表
    """
    name = models.CharField(max_length=24)
    publisher = models.ForeignKey(to="Publisher")

    def __str__(self):
        return self.name


class Author(models.Model):
    """
    作者表
    """
    name = models.CharField(max_length=24)
    books = models.ManyToManyField(to="Book", related_name="authors")




