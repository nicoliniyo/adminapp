from rest_framework import serializers
from .models import Actividad  # Assuming your Actividad model is in the same app

class ActividadSerializer(serializers.ModelSerializer):
    created_by_user = serializers.SlugRelatedField(slug_field='username', read_only=True)  # Use username for user identification
    operated_by_user = serializers.SlugRelatedField(slug_field='username', read_only=True, allow_null=True)  # Allow null for operated_by

    class Meta:
        model = Actividad
        fields = '__all__'  # Include all fields

class ShortActividadSerializer(serializers.ModelSerializer):
    created_by_user = serializers.SlugRelatedField(slug_field='username', read_only=True)  # Use username for user identification

    class Meta:
        model = Actividad
        fields = ['id', 'created_at', 'activity_type', 'status', 'created_by_user']  # Select specific fields
