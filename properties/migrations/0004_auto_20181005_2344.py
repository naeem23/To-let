# Generated by Django 2.0.2 on 2018-10-05 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_auto_20181003_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='available_from',
            field=models.DateTimeField(),
        ),
    ]