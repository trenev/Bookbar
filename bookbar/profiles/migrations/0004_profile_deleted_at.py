# Generated by Django 4.0.3 on 2022-03-18 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_first_name_alter_profile_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
