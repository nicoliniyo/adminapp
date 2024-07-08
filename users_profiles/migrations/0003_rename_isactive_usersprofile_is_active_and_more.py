# Generated by Django 5.0.6 on 2024-06-28 09:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_profiles', '0002_usersprofile_local_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersprofile',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='usersprofile',
            old_name='isAdmin',
            new_name='is_admin',
        ),
        migrations.RenameField(
            model_name='usersprofile',
            old_name='lastName1',
            new_name='last_name1',
        ),
        migrations.RenameField(
            model_name='usersprofile',
            old_name='lastName2',
            new_name='last_name2',
        ),
        migrations.RenameField(
            model_name='usersprofile',
            old_name='phonePersonal',
            new_name='phone_personal',
        ),
        migrations.AddField(
            model_name='usersprofile',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]