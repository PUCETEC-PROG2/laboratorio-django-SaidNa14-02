# Generated by Django 4.2 on 2024-12-21 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('level', models.PositiveSmallIntegerField()),
                ('birth_date', models.DateField()),
            ],
        ),
    ]
