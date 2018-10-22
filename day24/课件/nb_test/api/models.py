from django.db import models


class Application(models.Model):
    """
    应用表：
        title ： 应用名称
    """
    title = models.CharField(verbose_name='应用名称', max_length=32)


class Api(models.Model):
    """
    API表：
        url : api地址
        app : api所属应用
    """
    url = models.CharField(verbose_name='API', max_length=255)
    app = models.ForeignKey(verbose_name='所属应用', to='Application')
