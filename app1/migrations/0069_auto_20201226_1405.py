# Generated by Django 2.2.7 on 2020-12-26 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0068_auto_20201226_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='resource_date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 26, 14, 5, 13, 411345)),
        ),
    ]
