# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 23:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20170505_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='corredor',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Categoria'),
        ),
        migrations.AddField(
            model_name='corredor',
            name='distancia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Distancia'),
        ),
        migrations.AddField(
            model_name='corredor',
            name='numero',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]