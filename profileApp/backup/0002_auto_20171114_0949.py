# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 07:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coursesApp', '0001_initial'),
        ('profileApp', '0001_initial'),
        ('sessionManagerApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersemester',
            name='info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sessionManagerApp.UserInfo'),
        ),
        migrations.AddField(
            model_name='completedcourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coursesApp.Course'),
        ),
        migrations.AddField(
            model_name='completedcourse',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profileApp.UserSemester'),
        ),
    ]
