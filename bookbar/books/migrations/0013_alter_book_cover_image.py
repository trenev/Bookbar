# Generated by Django 4.0.3 on 2022-04-08 19:36

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_rename_description_book_annotation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]