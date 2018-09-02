from django.db import models

# Create your models here.


class Employee1(models.Model):
    name = models.CharField(max_length=12)
    age = models.IntegerField()
    salary = models.IntegerField()
    dept = models.CharField(max_length=12)


class Dept(models.Model):
    name = models.CharField(max_length=12)


class Employee2(models.Model):
    name = models.CharField(max_length=12)
    age = models.IntegerField()
    salary = models.IntegerField()
    dept = models.ForeignKey(to="Dept")


class Book(models.Model):
    alex = models.DateTimeField()
