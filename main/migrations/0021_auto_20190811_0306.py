# Generated by Django 2.2.2 on 2019-08-10 21:36

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20190811_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
