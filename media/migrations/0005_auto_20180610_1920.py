# Generated by Django 2.0.5 on 2018-06-10 19:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0004_remove_media_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5000), size=None),
        ),
    ]
