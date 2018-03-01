# Generated by Django 2.0.2 on 2018-02-28 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessionManagerApp', '0004_chatfullname_user'),
        ('onlineExamsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlineexam',
            name='session',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sessionManagerApp.Session'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='exam',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='onlineExamsApp.OnlineExam'),
            preserve_default=False,
        ),
    ]
