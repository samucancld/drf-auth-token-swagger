"""
Views for the recipe APIs
"""

from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from common.models import Recipe, Tag
from . import serializers
from rest_framework import serializers as drf_serializers

class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs"""

    serializer_class = serializers.RecipeDetailedSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes only for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by("-id")

    def get_serializer_class(self):
        """Return the serializer class for request"""

        match self.action:
            case "list":
                return serializers.RecipeListedSerializer
            case "create" | "partial_update" | "update" | "destroy" :
                return serializers.RecipeModelSerializer
            case "retrieve":
                return serializers.RecipeDetailedSerializer

    def perform_create(self, serializer):
        """Create a new recipe"""

        serializer.save(user=self.request.user)

class TagViewSet(viewsets.ModelViewSet):
    """Manage tags in the database"""

    serializer_class = serializers.TagBaseSerializer
    queryset = Tag.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """Return the serializer class for request"""

        match self.action:
            case "list":
                return serializers.TagListedSerializer
            case "create" | "partial_update" | "update" | "destroy":
                return serializers.TagBaseSerializer
            case "retrieve":
                return serializers.TagDetailedSerializer

    def perform_create(self, serializer):
        """Create a new tag"""
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """Retrieve tags for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by("-name")
