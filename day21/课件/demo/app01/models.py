from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=12)


class Book(models.Model):
    title = models.CharField(max_length=12)
    publisher = models.ForeignKey(to="Publisher", on_delete=models.CASCADE)
    num = models.IntegerField(default=0)

    keep_num = models.IntegerField(verbose_name="收藏数", default=0)
    comment_num = models.IntegerField(verbose_name="评论数", default=0)


    def __str__(self):
        return self.title


