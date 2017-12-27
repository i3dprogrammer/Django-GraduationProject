# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='#A312', max_length=15, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('elective', models.BooleanField(default=False)),
                ('duration', models.TimeField()),
                ('applications_duration', models.TimeField()),
                ('max_written_result', models.IntegerField(default=70)),
                ('max_oral_result', models.IntegerField(default=10)),
                ('max_app_result', models.IntegerField(default=20)),
                ('info', models.TextField(max_length=1000)),
                ('prequels', models.ManyToManyField(blank=True, related_name='_course_prequels_+', to='coursesApp.Course')),
            ],
        ),
    ]