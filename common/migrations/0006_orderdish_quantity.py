# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20170521_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdish',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
