# Generated by Django 3.1.2 on 2021-01-18 07:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0079_auto_20210118_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_Codechef_id',
        ),
        migrations.AlterField(
            model_name='resources',
            name='resource_date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 18, 13, 21, 42, 254493)),
        ),
    ]
