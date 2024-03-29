# Generated by Django 2.0.2 on 2018-10-11 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0007_auto_20181006_0102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='feature',
        ),
        migrations.AddField(
            model_name='feature',
            name='broad_band',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='feature',
            name='garage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='feature',
            name='generator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='feature',
            name='lift',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='feature',
            name='security',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='feature',
            name='telephone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='features',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.Feature'),
        ),
    ]
