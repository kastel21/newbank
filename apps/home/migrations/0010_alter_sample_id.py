# Generated by Django 3.2.13 on 2022-08-25 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_sample_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
