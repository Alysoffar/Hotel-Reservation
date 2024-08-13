# Generated by Django 5.0.7 on 2024-08-13 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_creationdate_customer_creation_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
