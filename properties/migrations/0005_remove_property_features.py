# Generated by Django 2.0.2 on 2018-10-05 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_auto_20181005_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='features',
        ),
    ]