# Generated by Django 3.1.2 on 2021-01-04 12:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0075_auto_20210104_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_portfolio',
        ),
        migrations.AlterField(
            model_name='resources',
            name='resource_date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 4, 18, 17, 47, 110414)),
        ),
    ]
