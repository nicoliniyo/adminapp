# noinspection PyInterpreter
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User  # Import User model for relationships

class Actividad(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp on creation
    created_by_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_actividades')  # Foreign key to User model
    # created_by_full_name = models.CharField(max_length=255, blank=True, null=True)  # Optional full name

    # Consider adding phone number as a separate model (optional)
    created_by_phone = models.CharField(max_length=20, blank=True, null=True)

    # Consider using GeoDjango for location fields (optional)
    created_by_lat = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    created_by_long = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)

    # Consider using a separate Address model (optional)
    created_by_address = models.CharField(max_length=255, blank=True, null=True)

    activity_type = models.CharField(max_length=255)
    status = models.IntegerField()  # Use IntegerField for status code
    operated_by_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='operated_actividades', blank=True, null=True)  # Optional foreign key for operated_by
    material_type = models.CharField(max_length=255)
    material_volume = models.IntegerField()
    material_unit = models.CharField(max_length=255)

    class Meta:
        ordering = ['-created_at']  # Default ordering by creation time (descending)

    def __str__(self):
        return f"Id: {self.id} - {self.activity_type} - UserId: {self.created_by_user}"  # User-friendly string representation
