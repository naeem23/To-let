# Generated by Django 2.1.4 on 2019-06-26 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0014_auto_20181206_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
