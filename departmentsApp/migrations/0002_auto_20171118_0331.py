# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 01:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departmentsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='prequel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departmentsApp.Group'),
        ),
    ]
