# Generated by Django 3.1.1 on 2020-09-30 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200925_0204'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='email',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='resident',
            name='passcode',
            field=models.CharField(blank=True, default=3666, max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
    ]
