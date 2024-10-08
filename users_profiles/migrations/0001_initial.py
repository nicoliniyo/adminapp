# Generated by Django 5.0.6 on 2024-06-27 16:14

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('names', models.CharField(max_length=255)),
                ('lastName1', models.CharField(max_length=100)),
                ('lastName2', models.CharField(blank=True, max_length=100)),
                ('phonePersonal', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('address_lat', models.FloatField(blank=True, null=True)),
                ('address_long', models.FloatField(blank=True, null=True)),
                ('additional_information', models.TextField(blank=True)),
                ('subscribed_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_type', models.CharField(choices=[('standard', 'Standard User'), ('admin', 'Admin')], default='standard', max_length=10)),
                ('isAdmin', models.BooleanField(default=False)),
                ('isActive', models.BooleanField(default=True)),
                ('date_of_birth', models.DateField()),
                ('document_number', models.CharField(max_length=50, unique=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
