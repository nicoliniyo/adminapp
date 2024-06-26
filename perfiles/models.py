from django.db import models

# Create your models here.
from django.contrib.auth.models import User  # Import the User model for user association
from django.db import models
from django.utils import timezone  # Use timezone for timestamps

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)  # Link to User model
    email = models.EmailField(max_length=255, unique=True)  # Ensure unique email

    # Separate first and last names for better data handling
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    phone_personal = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    address_lat = models.FloatField(blank=True, null=True)
    address_long = models.FloatField(blank=True, null=True)
    additional_information = models.TextField(blank=True)

    subscribed_on = models.DateTimeField(default=timezone.now)  # Use timezone.now() for accurate timestamp

    # Use choices for user type (consider adding more options as needed)
    USER_TYPE_CHOICES = (
        # ('standard', 'Standard User'),
        # ('admin', 'Admin'),
        ('ACTIVIDAD_TIPO_USUARIO_VECINO', 'VECINO'),
        ('ACTIVIDAD_TIPO_USUARIO_RECOLECTOR', 'RECOLECTOR'),
        ('ACTIVIDAD_TIPO_USUARIO_ADMIN', 'ADMIN'),
    )
    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICES, default='standard')

    # Use BooleanField for is_admin and is_active
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_of_birth = models.DateField(blank=True, null=True)  # Allow null/blank for date of birth
    document_number = models.CharField(max_length=50, unique=True)  # Unique document number
    local_user_id = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
