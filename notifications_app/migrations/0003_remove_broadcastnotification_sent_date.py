# Generated by Django 5.0.3 on 2024-08-11 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications_app', '0002_broadcastnotification_sent_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='broadcastnotification',
            name='sent_date',
        ),
    ]
