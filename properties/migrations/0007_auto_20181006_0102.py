# Generated by Django 2.0.2 on 2018-10-05 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_property_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='draft',
            field=models.BooleanField(default=True),
        ),
    ]