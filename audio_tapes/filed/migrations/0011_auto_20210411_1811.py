# Generated by Django 3.0.5 on 2021-04-11 18:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filed', '0010_auto_20210411_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='participants',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100, null=True), null=True, size=10),
        ),
    ]
