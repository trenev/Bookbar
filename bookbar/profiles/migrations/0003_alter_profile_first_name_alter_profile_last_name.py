# Generated by Django 4.0.3 on 2022-03-18 09:12

import bookbar.common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[
                bookbar.common.validators.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[
                bookbar.common.validators.validate_only_letters]),
        ),
    ]
