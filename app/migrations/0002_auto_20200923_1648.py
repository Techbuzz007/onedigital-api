# Generated by Django 3.1.1 on 2020-09-23 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='passcode',
            field=models.CharField(blank=True, default=5001, max_length=40, unique=True),
        ),
    ]
