# Generated by Django 3.1.2 on 2021-05-16 16:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0092_auto_20210516_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='user',
        ),
        migrations.AddField(
            model_name='idea',
            name='user',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resources',
            name='resource_date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 16, 22, 9, 22, 645894)),
        ),
    ]
