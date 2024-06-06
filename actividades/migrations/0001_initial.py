# Generated by Django 3.1.2 on 2024-06-02 21:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('created_by_lat', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('created_by_long', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('created_by_address', models.CharField(blank=True, max_length=255, null=True)),
                ('activity_type', models.CharField(max_length=255)),
                ('status', models.IntegerField()),
                ('material_type', models.CharField(max_length=255)),
                ('material_volume', models.IntegerField()),
                ('material_unit', models.CharField(max_length=255)),
                ('created_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_actividades', to=settings.AUTH_USER_MODEL)),
                ('operated_by_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='operated_actividades', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
