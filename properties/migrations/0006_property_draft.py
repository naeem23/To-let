# Generated by Django 2.0.2 on 2018-10-05 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_remove_property_features'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]
