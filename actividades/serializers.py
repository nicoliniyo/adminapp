from rest_framework import serializers
from .models import Actividad  # Assuming your Actividad model is in the same app
from django.contrib.auth.models import User

class ActividadSerializer(serializers.ModelSerializer):
    # created_by_user = serializers.SlugRelatedField(slug_field='id', queryset=User.objects.all())  # Use username for user identification
    # operated_by_user = serializers.SlugRelatedField(slug_field='id', read_only=True, allow_null=True)  # Allow null for operated_by

    def create(self, validated_data):
        # Your custom logic to retrieve or create a user object
        # based on data in validated_data (e.g., email)
        user = User.objects.get(id=validated_data['created_by_user_id'])  # Example
        validated_data['created_by_user_id'] = user
        return Actividad.objects.create(**validated_data)

    class Meta:
        model = Actividad
        fields = '__all__'  # Include all fields

    # def validate_created_by_user(self, value):
    #     # Ensure the user exists and is valid
    #     if not value:
    #         raise serializers.ValidationError("Created by user is required")
    #     return value


class ShortActividadSerializer(serializers.ModelSerializer):
    created_by_user = serializers.SlugRelatedField(slug_field='id', read_only=True)  # Use username for user identification

    class Meta:
        model = Actividad
        fields = ['id', 'created_at', 'activity_type', 'status', 'created_by_user']  # Select specific fields
