"""
Serializers for the the Recipe model
"""
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from common.models import Ingredient, Recipe, Tag

from .ingredient_serializers import (IngredientNestedCUDSerializer,
                                     IngredientRelatedSerializer)
from .tag_serializers import TagNestedCUDSerializer, TagRelatedSerializer


class RecipeBaseSerializer(serializers.ModelSerializer):
    """Base serializer for recipes. Contains all model fields plus self property
    and avoid id representation and description."""

    self = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Recipe
        fields = [
            "self",
            "title",
            "time_minutes",
            "price",
        ]
        read_only_fields = ["id"]

    def get_self(self, obj):
        return obj.self_url


class RecipeModelSerializer(RecipeBaseSerializer):
    """
    Model recipe serializer for C-U-D operations, contains all the
    model fields except the id
    """

    tags = TagNestedCUDSerializer(
        many=True,
        required=False,
    )

    ingredients = IngredientNestedCUDSerializer(
        many=True,
        required=False,
    )

    class Meta(RecipeBaseSerializer.Meta):
        fields = RecipeBaseSerializer.Meta.fields + [
            "description",
            "image",
            "tags",
            "ingredients",
        ]

    def _get_or_create_tags(self, tags, recipe):
        """Handle getting or creating tags as needed."""

        auth_user = self.context["request"].user
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(
                user=auth_user,
                **tag,  # same as name = tag['name']
            )
            recipe.tags.add(tag_obj)

        return recipe

    def _get_or_create_ingredients(self, ingredients, recipe):
        """Handle getting or creating ingredients as needed."""

        auth_user = self.context["request"].user
        for ingredient in ingredients:
            ingredient_obj, created = Ingredient.objects.get_or_create(
                user=auth_user,
                **ingredient,  # same as name = tag['name']
            )
            recipe.ingredients.add(ingredient_obj)

        return recipe

    def create(self, validated_data):
        """Creaste a recipe."""
        tags = validated_data.pop("tags", [])
        ingredients = validated_data.pop("ingredients", [])
        recipe = Recipe.objects.create(**validated_data)
        self._get_or_create_tags(tags, recipe)
        self._get_or_create_ingredients(ingredients, recipe)

        return recipe

    def update(self, instance, validated_data):
        """Update a recipe"""
        tags = validated_data.pop("tags", None)
        if tags is not None:
            instance.tags.clear()
            self._get_or_create_tags(tags, instance)

        ingredients = validated_data.pop("ingredients", None)
        if ingredients is not None:
            instance.ingredients.clear()
            self._get_or_create_ingredients(ingredients, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    def validate_title(self, value):
        """
        As this recipe model serializers is used to CUD operations, is it necessary
        to validate that doesn't exist a recipe with the same title for the current user
        """
        user = self.context["request"].user
        if not Recipe.objects.filter(user=user, title=value).exists():
            return value
        raise serializers.ValidationError(
            "Ya tenes registrada una receta con ese nombre"
        )


class RecipeListedSerializer(RecipeBaseSerializer):
    """
    Serializer for list operation for the recipe, just add links field to the
    base recipe serializer
    """

    links = serializers.SerializerMethodField(read_only=True)

    class Meta(RecipeBaseSerializer.Meta):
        fields = RecipeBaseSerializer.Meta.fields + ["links"]

    def get_links(self, obj):
        links = []
        for tag in obj.tags.all():
            links.append(
                {
                    "rel": "tag",
                    "href": tag.self_url,
                }
            )
        for ingredient in obj.ingredients.all():
            links.append(
                {
                    "rel": "ingredient",
                    "href": ingredient.self_url,
                }
            )
        return links


class RecipeDetailedSerializer(RecipeBaseSerializer):
    """
    Serializer for recipe detail view. Just add nested tag serializer
    """

    tags = TagRelatedSerializer(
        many=True,
    )

    ingredients = IngredientRelatedSerializer(many=True)

    class Meta(RecipeBaseSerializer.Meta):
        fields = RecipeBaseSerializer.Meta.fields + [
            "description",
            "tags",
            "ingredients",
        ]


class RecipeRelatedSerializer(RecipeBaseSerializer):
    pass
