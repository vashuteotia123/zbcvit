# Generated by Django 3.0.6 on 2020-06-17 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_seen_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seen_notification',
            old_name='Notification_id',
            new_name='Notification',
        ),
    ]
