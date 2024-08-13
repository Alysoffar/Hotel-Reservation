# Generated by Django 5.0.7 on 2024-08-12 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='CreationDate',
            new_name='creation_date',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='customer',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='image',
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics'),
        ),
    ]
