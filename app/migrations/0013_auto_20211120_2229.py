# Generated by Django 3.2.7 on 2021-11-20 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20211120_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='timein',
            field=models.IntegerField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='feature',
            name='timeout',
            field=models.IntegerField(max_length=50, null=True),
        ),
    ]
