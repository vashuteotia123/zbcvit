# Generated by Django 2.2.7 on 2020-10-26 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0049_auto_20201026_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='resource_date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 26, 22, 13, 16, 620214)),
        ),
    ]
