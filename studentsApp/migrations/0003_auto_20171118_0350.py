# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 01:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentsApp', '0002_auto_20171118_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='group',
            field=models.ForeignKey(default=23, on_delete=django.db.models.deletion.CASCADE, to='departmentsApp.Group'),
        ),
    ]
