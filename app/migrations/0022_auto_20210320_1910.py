# Generated by Django 3.1.7 on 2021-03-20 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20210320_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='passcode',
            field=models.CharField(blank=True, default=9156, max_length=120, unique=True),
        ),
    ]
