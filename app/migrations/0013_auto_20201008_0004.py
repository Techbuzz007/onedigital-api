# Generated by Django 3.1.1 on 2020-10-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20201008_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='passcode',
            field=models.CharField(blank=True, default=4823, max_length=120, unique=True),
        ),
    ]
