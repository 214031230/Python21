# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-21 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20180815_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='products',
            field=models.ManyToManyField(related_name='userinfos', to='user.Product'),
        ),
    ]
