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

    # def create(self, validated_data):
    #     user_data = validated_data.pop('user')
    #     user = User.objects.create(**user_data)
    #     perfil = Perfil.objects.create(user=user, **validated_data)
    #     return perfil
    #
    # def update(self, instance, validated_data):
    #     user_data = validated_data.pop('user')
    #     instance.user.username = user_data.get('username', instance.user.username)
    #     instance.user.email = user_data.get('email', instance.user.email)
    #     instance.user.save()
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     instance.address = validated_data.get('address', instance.address)
    #     # Update other fields as necessary
    #     instance.save()
    #     return instance
        # Optional: Customize field validation or behavior here
        # e.g., validators for phone number format
