# Generated by Django 2.0.5 on 2018-06-20 19:29

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0006_auto_20180619_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5000), blank=True, null=True, size=None),
        ),
    ]