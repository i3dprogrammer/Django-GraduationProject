# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 00:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsApp', '0003_auto_20171118_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='full_name',
            field=models.CharField(default='Ahmed Magdy Mohammed Essa', max_length=100),
        ),
    ]
