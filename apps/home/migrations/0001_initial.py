# Generated by Django 3.2.13 on 2022-08-24 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Freezer',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('capacity', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('shelves', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('dob', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('n/a', 'n/a')], max_length=10)),
                ('phone', models.CharField(default='0783872345', max_length=20)),
                ('age', models.CharField(default='1', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('narrative_name', models.CharField(default='sadf asd fadfg arsg dvadhf dgjhbn', max_length=500)),
                ('status', models.CharField(choices=[('On going', 'On going'), ('Ended', 'Ended'), ('n/a', 'n/a')], default='On going', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('capacity', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('racks', models.IntegerField()),
                ('freezer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.freezer')),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
                ('date_of_archive', models.CharField(max_length=200)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.patient')),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.study')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='study',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.study'),
        ),
        migrations.CreateModel(
            name='Cube',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('occupied', models.BooleanField(default=False)),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.box')),
                ('freezer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.freezer')),
                ('rack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.rack')),
                ('sample', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.sample')),
                ('shelf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.shelf')),
            ],
        ),
        migrations.AddField(
            model_name='box',
            name='freezer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.freezer'),
        ),
        migrations.AddField(
            model_name='box',
            name='rack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.rack'),
        ),
        migrations.AddField(
            model_name='box',
            name='shelf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.shelf'),
        ),
    ]
