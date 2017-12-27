# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('written_result', models.IntegerField()),
                ('oral_result', models.IntegerField()),
                ('app_result', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PublicNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showToStudents', models.BooleanField(default=True)),
                ('showToProfessors', models.BooleanField(default=False)),
                ('notification', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserSemester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GPA', models.FloatField(default=0.0)),
            ],
        ),
    ]
