# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departmentsApp', '0003_department_dep_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dep_name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
