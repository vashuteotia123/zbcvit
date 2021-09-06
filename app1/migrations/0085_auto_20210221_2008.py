# Generated by Django 3.1.2 on 2021-02-21 14:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0084_auto_20210213_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='resource_date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 21, 20, 8, 36, 921649)),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_Codechef_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_Codeforces_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]