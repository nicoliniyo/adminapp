from rest_framework import serializers
from .models import UsersProfile
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        # Your custom logic to retrieve or create a user object
        # based on data in validated_data (e.g., email)
        user = User.objects.get(email=validated_data['email'])  # Example
        validated_data['user'] = user
        return UsersProfile.objects.create(**validated_data)

    class Meta:
        model = UsersProfile
        fields = (
            'id', 'email', 'created_at', 'names', 'last_name1', 'last_name2', 'phone_personal',
            'address', 'address_lat', 'address_long', 'additional_information',
            'subscribed_on', 'user_type', 'is_admin', 'is_active', 'user_id', 'date_of_birth',
            'document_number', 'local_user_id'
        )

        # Optional fields for user linking
        # user = serializers.ReadOnlyField(source='user.username')
        # 'user', 'email', 'first_name', 'last_name', 'phone_personal', 'address',
        # 'address_lat', 'address_long', 'additional_information', 'subscribed_on',
        # 'user_type', 'is_admin', 'is_active', 'date_of_birth', 'document_number'
        # Consider adding custom validation for specific fields (e.g., email format)
