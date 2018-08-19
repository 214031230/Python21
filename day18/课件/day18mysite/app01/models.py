from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=24)
    price = models.IntegerField()


class Publisher(models.Model):
    name = models.CharField(max_length=24)
