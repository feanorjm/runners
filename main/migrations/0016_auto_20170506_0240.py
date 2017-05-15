# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20170506_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corredor',
            name='ciudad',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='corredor',
            name='correo',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='corredor',
            name='pais',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='corredor',
            name='telefono',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
