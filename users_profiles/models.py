from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .custom_fields import EpochDateTimeField
 # Assuming custom_fields.py is in the same directory
# YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z].
class UsersProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)  # Optional, for linking profiles to users
    email = models.EmailField(max_length=255, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    names = models.CharField(max_length=255)
    last_name1 = models.CharField(max_length=100)
    last_name2 = models.CharField(max_length=100, blank=True)
    phone_personal = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    address_lat = models.FloatField(blank=True, null=True)
    address_long = models.FloatField(blank=True, null=True)
    additional_information = models.TextField(blank=True)
    subscribed_on = models.DateTimeField(default=timezone.now)

    USER_TYPE_CHOICES = (
        ('VECINO', 'Vecino'),
        ('RECOLECTOR', 'Recolector'),
        ('ADMIN', 'Admin'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='standard')
    is_admin = models.BooleanField(default=False)  # Use `isAdmin` instead of `is_admin` for consistency
    is_active = models.BooleanField(default=True)  # Use `isActive` instead of `is_active` for consistency
    date_of_birth = models.DateField()  # Assuming date of birth is required
    document_number = models.CharField(max_length=50, unique=True)
    local_user_id = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Id: {self.id} UserId: {self.user} {self.names} {self.last_name1} ({self.email}) - {self.local_user_id}"



