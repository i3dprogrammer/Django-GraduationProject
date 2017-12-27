# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=100)),
                ('news_desc', models.CharField(max_length=5000)),
                ('news_date', models.DateTimeField(verbose_name='Date published')),
            ],
        ),
    ]