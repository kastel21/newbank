# Generated by Django 3.2.13 on 2022-08-25 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rack',
            name='freezer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.freezer'),
        ),
    ]