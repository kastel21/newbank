# Generated by Django 3.2.13 on 2022-08-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_sample_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='name',
        ),
        migrations.AlterField(
            model_name='sample',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
