# Generated by Django 3.0.5 on 2021-04-11 13:45

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='participants',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=[], size=10),
        ),
    ]
