# Generated by Django 3.1.2 on 2020-10-21 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20201021_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='vehicle_number',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='resident',
            name='passcode',
            field=models.CharField(blank=True, default=2917, max_length=120, unique=True),
        ),
    ]
