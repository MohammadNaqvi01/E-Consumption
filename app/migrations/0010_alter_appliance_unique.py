# Generated by Django 3.2.7 on 2021-11-20 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_appliance_unique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliance',
            name='unique',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.otp'),
        ),
    ]
