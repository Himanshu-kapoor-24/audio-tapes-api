# Generated by Django 3.0.5 on 2021-04-11 14:58

from django.db import migrations, models
import filed.models


class Migration(migrations.Migration):

    dependencies = [
        ('filed', '0006_auto_20210411_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audibook',
            name='uploaded_date',
            field=models.DateTimeField(validators=[filed.models.cannot_be_outdated]),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='uploaded_date',
            field=models.DateTimeField(validators=[filed.models.cannot_be_outdated]),
        ),
        migrations.AlterField(
            model_name='song',
            name='uploaded_date',
            field=models.DateTimeField(validators=[filed.models.cannot_be_outdated]),
        ),
    ]
