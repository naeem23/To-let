# Generated by Django 2.0.2 on 2018-10-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='floor_no',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
