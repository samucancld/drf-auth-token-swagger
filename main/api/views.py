"""
Views that handle each endpoint of the API
"""
from django.shortcuts import render
from rest_framework import (
    generics,
    authentication,
    permissions,
)
from rest_framework.permissions import (
    # IsAuthenticatedOrReadOnly,
    IsAdminUser,
    IsAuthenticated,
)
from rest_framework.settings import api_settings
from rest_framework.authtoken import views as token_views
from .serializers import TokenSerializer, UserSerializer
from django.contrib.auth import get_user_model

# Create your views here.



class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system with POST."""
    serializer_class = UserSerializer

class ListUserView(generics.ListAPIView):
    """Retrieve the list of users with GET (just for admins)"""
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]


class RetrieveUpdateUserView(generics.RetrieveUpdateAPIView):
    """Retrieve user data with GET and update user data with PUT/PATCH."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user"""
        return self.request.user

class RetrieveCreateTokenView(token_views.ObtainAuthToken):
    """Crate a new auth token for user or retrieve the existent."""

    serializer_class = TokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

