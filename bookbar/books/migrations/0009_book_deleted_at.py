# Generated by Django 4.0.3 on 2022-03-18 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_book_author_alter_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
