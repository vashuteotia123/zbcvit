# Generated by Django 3.1.2 on 2021-05-09 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0089_auto_20210426_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='resource_date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 9, 17, 32, 30, 685929)),
        ),
        migrations.AlterField(
            model_name='user',
            name='events_reg',
            field=models.ManyToManyField(blank=True, null=True, related_name='events_id', to='app1.Event'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_github',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_insta',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_linkedin',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]