from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Perfil
from .serializers import PerfilSerializer

# Create your views here.
class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.select_related('user')  # Pre-fetch related user data for efficiency
    serializer_class = PerfilSerializer

    # Permission classes to control access
    permission_classes = [permissions.IsAuthenticated]  # Require authentication for all actions

    # Optional: Override specific viewset methods for custom logic
    # e.g., filtering, pagination, custom actions
