# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 00:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departmentsApp', '0001_initial'),
        ('coursesApp', '0007_remove_course_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='departmentsApp.Group'),
        ),
    ]
