# Generated by Django 3.2.5 on 2022-08-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_sample_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]