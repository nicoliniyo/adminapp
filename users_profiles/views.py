from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import UsersProfile
from .serializer import UserProfileSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UsersProfile.objects.select_related('user')  # Pre-fetch related user data (optional)
    serializer_class = UserProfileSerializer
    filterset_fields = ('document_number',)

    permission_classes = [permissions.IsAuthenticated]  # Set appropriate permissions