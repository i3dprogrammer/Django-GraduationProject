# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coursesApp', '0002_auto_20171116_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='coursesApp.Group'),
        ),
    ]