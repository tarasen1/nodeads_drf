# Generated by Django 2.1.3 on 2018-11-13 17:42

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('my_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Elements',
            new_name='Element',
        ),
        migrations.RenameModel(
            old_name='Groups',
            new_name='Group',
        ),
    ]
