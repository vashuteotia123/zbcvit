# Generated by Django 3.0.6 on 2020-06-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_auto_20200622_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_photos',
            name='event_photo',
            field=models.ImageField(null=True, upload_to='app1/static/media/events_images/'),
        ),
    ]
