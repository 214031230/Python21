from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32)


class Order(models.Model):
    title = models.CharField(max_length=32)
