# Generated by Django 5.0.3 on 2024-08-11 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications_app', '0005_alter_broadcastnotification_broadcast_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='broadcastnotification',
            name='sent',
        ),
    ]
