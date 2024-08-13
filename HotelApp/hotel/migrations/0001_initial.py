# Generated by Django 5.0.7 on 2024-08-11 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('RestaurantsBarsNo', models.IntegerField()),
                ('Satisfied_Guests', models.IntegerField()),
            ],
        ),
    ]