# Generated by Django 2.2.7 on 2020-10-26 16:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0047_auto_20201023_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_insta',
            field=models.CharField(default='#', max_length=5000),
        ),
        migrations.AlterField(
            model_name='resources',
            name='resource_date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 26, 22, 9, 54, 622758)),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_github',
            field=models.CharField(default='#', max_length=5000),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_linkedin',
            field=models.CharField(default='#', max_length=5000),
        ),
    ]
