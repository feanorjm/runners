# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170502_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corredor',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
