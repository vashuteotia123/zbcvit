# Generated by Django 3.1.2 on 2021-01-30 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0081_auto_20210118_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_Codechef_id',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='user_Codeforces_id',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='non_vitians',
            name='email_id',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='resources',
            name='resource_date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 30, 17, 24, 9, 854641)),
        ),
    ]
