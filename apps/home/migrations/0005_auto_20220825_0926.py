# Generated by Django 3.2.13 on 2022-08-25 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220825_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='box',
            name='freezer',
        ),
        migrations.RemoveField(
            model_name='box',
            name='shelf',
        ),
    ]
