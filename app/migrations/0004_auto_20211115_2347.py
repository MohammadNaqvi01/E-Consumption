# Generated by Django 3.2.7 on 2021-11-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211115_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restmodel',
            name='timein',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='restmodel',
            name='timeout',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
