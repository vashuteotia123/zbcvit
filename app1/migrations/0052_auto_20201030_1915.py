# Generated by Django 2.2.7 on 2020-10-30 13:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0051_auto_20201027_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='resource_date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 30, 19, 15, 39, 862458)),
        ),
    ]
