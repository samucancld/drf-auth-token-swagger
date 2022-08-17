"""
Serializers for the the Ingredient model
"""
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from common.models import Ingredient


class IngredientBaseSerializer(serializers.ModelSerializer):
    """Serializer for ingredients used to C-R-U-Detail operations."""

    self = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Ingredient
        fields = [
            "self",
            "name",
        ]
        print(fields)

    def get_self(self, obj):
        """Get self_url property"""
        return obj.self_url

    def validate_name(self, value):
        """Validate that doesn't exists an ingredient with the same name for the current user"""
        user = self.context["request"].user
        if not Ingredient.objects.filter(user=user, name=value).exists():
            return value
        raise serializers.ValidationError(
            "Ingredient already registered with that name"
        )


class IngredientNestedCUDSerializer(IngredientBaseSerializer):
    """Serializer for ingredients used to nested CUD operations."""

    def validate_name(self, value):
        """As this serializer is used to CUD nested operations, e.g. when creating a recipe,
        it's not necessary to check that the user already have an ingredient with the name, because
        that validations is made in the recipemodelserializer when call to his method _get_or_create_ingredients"""
        return value


class IngredientListedSerializer(IngredientBaseSerializer):
    """Serializer for ingredient list operation."""

    links = serializers.SerializerMethodField(read_only=True)

    class Meta(IngredientBaseSerializer.Meta):
        fields = IngredientBaseSerializer.Meta.fields + [
            "links",
        ]

    def get_links(self, obj):
        """Get all links for related recipes"""
        links = []
        for recipe in obj.recipes.all():
            links.append(
                {
                    "rel": "recipe",
                    "href": recipe.self_url,
                }
            )
        return links


# Ingredient Serialization Aliases:
## Alias for retrieve operation
IngredientDetailedSerializer = IngredientListedSerializer
## Alias for nested serialization
IngredientRelatedSerializer = IngredientBaseSerializer
