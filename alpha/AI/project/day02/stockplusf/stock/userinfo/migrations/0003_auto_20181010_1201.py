# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-10 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_auto_20180930_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='tradepwd',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='交易密码'),
        ),
    ]