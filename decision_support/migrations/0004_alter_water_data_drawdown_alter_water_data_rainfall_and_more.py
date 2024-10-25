# Generated by Django 5.0.3 on 2024-05-15 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decision_support', '0003_alter_business_zones_business_zones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='water_data',
            name='Drawdown',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='water_data',
            name='Rainfall',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='water_data',
            name='WaterLevel',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
