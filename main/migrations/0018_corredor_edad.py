# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20170506_0245'),
    ]

    operations = [
        migrations.AddField(
            model_name='corredor',
            name='edad',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
