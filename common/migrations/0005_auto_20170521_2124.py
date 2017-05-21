# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20170521_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='weight',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]