# Generated by Django 3.2.13 on 2022-08-25 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220825_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='name',
            field=models.CharField(default='box 1', max_length=200),
        ),
        migrations.AddField(
            model_name='cube',
            name='name',
            field=models.CharField(default='cube 1', max_length=200),
        ),
        migrations.AddField(
            model_name='rack',
            name='name',
            field=models.CharField(default='rack 1', max_length=100),
        ),
    ]