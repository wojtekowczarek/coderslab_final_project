# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 05:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderslab', '0003_auto_20171128_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 28, 5, 40, 49, 316029)),
        ),
    ]
