# Generated by Django 4.2 on 2023-04-22 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MenuTable',
            new_name='MenuItem',
        ),
    ]