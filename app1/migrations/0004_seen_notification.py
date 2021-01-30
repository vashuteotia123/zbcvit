# Generated by Django 3.0.6 on 2020-06-17 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_user_user_join_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seen_notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Notification_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Notification')),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.User')),
            ],
        ),
    ]
