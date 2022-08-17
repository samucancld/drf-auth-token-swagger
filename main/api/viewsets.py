"""
Views for the recipe APIs
"""

from rest_framework import serializers as drf_serializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api.serializers import (ingredient_serializers, recipe_serializers,
                             tag_serializers)
from common.models import Ingredient, Recipe, Tag


class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs"""

    serializer_class = recipe_serializers.RecipeDetailedSerializer
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
                return recipe_serializers.RecipeListedSerializer
            case "create" | "partial_update" | "update" | "destroy":
                return recipe_serializers.RecipeModelSerializer
            case "retrieve":
                return recipe_serializers.RecipeDetailedSerializer

    def perform_create(self, serializer):
        """Create a new recipe"""

        serializer.save(user=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    """Manage tags in the database"""

    serializer_class = tag_serializers.TagBaseSerializer
    queryset = Tag.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """Return the serializer class for request"""

        match self.action:
            case "list":
                return tag_serializers.TagListedSerializer
            case "create" | "partial_update" | "update" | "destroy":
                return tag_serializers.TagBaseSerializer
            case "retrieve":
                return tag_serializers.TagDetailedSerializer

    def perform_create(self, serializer):
        """Create a new tag"""
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """Retrieve tags for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by("-name")


class IngredientViewSet(viewsets.ModelViewSet):
    """Manage ingredients in the database"""

    serializer_class = ingredient_serializers.IngredientBaseSerializer
    queryset = Ingredient.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """Return the serializer class for request"""

        match self.action:
            case "list":
                return ingredient_serializers.IngredientListedSerializer
            case "create" | "partial_update" | "update" | "destroy":
                return ingredient_serializers.IngredientBaseSerializer
            case "retrieve":
                return ingredient_serializers.IngredientDetailedSerializer

    def perform_create(self, serializer):
        """Create a new ingredient"""
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """Retrieve ingredients for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by("-name")
