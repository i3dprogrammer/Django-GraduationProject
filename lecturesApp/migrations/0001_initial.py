# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 18:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sessionManagerApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='lectures/%Y/%m/%d/%H/%M/')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sessionManagerApp.Session')),
            ],
        ),
    ]
