# Generated by Django 4.0.3 on 2022-04-15 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_alter_book_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category_name']},
        ),
    ]
