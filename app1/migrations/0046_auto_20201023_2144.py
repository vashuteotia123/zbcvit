# Generated by Django 2.2.7 on 2020-10-23 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0045_auto_20201023_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='resource_date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 23, 21, 44, 59, 462792)),
        ),
    ]
