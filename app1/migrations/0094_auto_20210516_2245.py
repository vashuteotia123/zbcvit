# Generated by Django 3.1.2 on 2021-05-16 17:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0093_auto_20210516_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='resource_date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 16, 22, 45, 24, 519608)),
        ),
    ]
