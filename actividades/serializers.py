from rest_framework import serializers
from .models import Actividad  # Assuming your Actividad model is in the same app
from django.contrib.auth.models import User

class ActividadSerializer(serializers.ModelSerializer):
    # def validate_created_by_user_id(self, value):
    #     try:
    #         User.objects.get(pk=value)
    #         return value
    #     except User.DoesNotExist:
    #         raise serializers.ValidationError("Invalid created_by_user_id")

    def create(self, validated_data):
        user_id = validated_data.get('created_by_user_id')

        if user_id:
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                raise serializers.ValidationError("Invalid created_by_user_id")
        else:
            # Handle the case where created_by_user_id is missing
            # For example, set a default user or raise an error
            user = None  # Or set a default user
            #raise serializers.ValidationError("created_by_user_id is required")  # Uncomment if required

        # Create the Actividad instance with the user or without
        actividad = Actividad.objects.create(**validated_data)
        if user:
            actividad.created_by_user = user
            actividad.save()
        return actividad



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
