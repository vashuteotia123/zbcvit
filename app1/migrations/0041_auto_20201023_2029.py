# Generated by Django 2.2.7 on 2020-10-23 14:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0040_auto_20201022_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='resource_date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 23, 20, 29, 53, 104040)),
        ),
    ]
