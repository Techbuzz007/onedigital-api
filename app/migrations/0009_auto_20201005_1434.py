# Generated by Django 3.1.1 on 2020-10-05 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20201005_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_agent_checkin', to='app.resident'),
        ),
        migrations.AlterField(
            model_name='resident',
            name='passcode',
            field=models.CharField(blank=True, default=2322, max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='resident',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visitor_agent_checkin', to='app.resident'),
        ),
    ]
