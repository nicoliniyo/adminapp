from rest_framework import serializers
from .models import Perfil

class PerfilSerializer(serializers.ModelSerializer):
    # Include only desired fields (consider security implications)
    user = serializers.ReadOnlyField(source='user.username')  # Only return username
    subscribed_on = serializers.DateTimeField(read_only=True)  # Read-only field for timestamp
    is_admin = serializers.BooleanField(read_only=True)  # Read-only for security

    class Meta:
        model = Perfil
        fields = (
            'user', 'email', 'first_name', 'last_name', 'phone_personal', 'address',
            'address_lat', 'address_long', 'additional_information', 'subscribed_on',
            'user_type', 'is_admin', 'is_active', 'date_of_birth', 'document_number'
        )

        # Optional: Customize field validation or behavior here
        # e.g., validators for phone number format
