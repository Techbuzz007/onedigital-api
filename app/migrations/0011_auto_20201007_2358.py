# Generated by Django 3.1.1 on 2020-10-07 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20201005_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='override',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='resident',
            name='passcode',
            field=models.CharField(blank=True, default=2525, max_length=120, unique=True),
        ),
    ]