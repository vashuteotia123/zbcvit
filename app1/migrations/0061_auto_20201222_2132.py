# Generated by Django 2.2.7 on 2020-12-22 16:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0060_auto_20201222_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='resource_date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 22, 21, 32, 47, 470646)),
        ),
    ]
