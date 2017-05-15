# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170503_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='TblComuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'tbl_comuna',
            },
        ),
        migrations.CreateModel(
            name='TblProvincia',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=23, null=True)),
            ],
            options={
                'db_table': 'tbl_provincia',
            },
        ),
        migrations.CreateModel(
            name='TblRegion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('iso_3166_2_cl', models.CharField(blank=True, db_column='ISO_3166_2_CL', max_length=5, null=True)),
            ],
            options={
                'db_table': 'tbl_region',
            },
        ),
    ]
