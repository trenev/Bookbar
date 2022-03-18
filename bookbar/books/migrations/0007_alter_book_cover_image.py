# Generated by Django 4.0.3 on 2022-03-17 21:13

import bookbar.books.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_book_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(upload_to='images/', validators=[bookbar.books.validators.MaxFileSizeInMBValidator(1)]),
        ),
    ]
