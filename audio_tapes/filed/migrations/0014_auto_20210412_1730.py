# Generated by Django 3.0.5 on 2021-04-12 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filed', '0013_auto_20210411_1818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audiobook',
            old_name='id',
            new_name='file_id',
        ),
        migrations.RenameField(
            model_name='podcast',
            old_name='id',
            new_name='file_id',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='id',
            new_name='file_id',
        ),
    ]