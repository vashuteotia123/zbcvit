# Generated by Django 3.0.6 on 2020-06-18 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20200617_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notification_seen',
            field=models.ManyToManyField(to='app1.User'),
        ),
        migrations.DeleteModel(
            name='Seen_notification',
        ),
    ]
