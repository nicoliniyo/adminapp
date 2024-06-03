from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated  # Optional permission class

from .models import Actividad
from .serializers import ActividadSerializer, ShortActividadSerializer


class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    permission_classes = [IsAuthenticated]  # Optional permission class for authentication
    serializer_class = ActividadSerializer  # Default serializer for most actions

    def get_serializer_class(self):
        """
        Override serializer based on action (optional for different representations)
        """
        if self.action == 'list':
            return ShortActividadSerializer
        return super().get_serializer_class()

