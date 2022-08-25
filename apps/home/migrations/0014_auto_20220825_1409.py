# Generated by Django 3.2.13 on 2022-08-25 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20220825_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='aliquoted',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Sample_Aliquote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_archive', models.CharField(max_length=200)),
                ('main_sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.sample')),
            ],
        ),
    ]