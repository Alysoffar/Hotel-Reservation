# Generated by Django 5.0.7 on 2024-08-17 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoomsBooking', '0002_remove_rooms_images_rooms_view_alter_rooms_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistration',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='RoomsBooking.rooms'),
        ),
    ]