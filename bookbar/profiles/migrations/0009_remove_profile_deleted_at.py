# Generated by Django 4.0.3 on 2022-04-08 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_profile_deleted_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='deleted_at',
        ),
    ]