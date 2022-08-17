"""
Serializers for the tag Model
"""

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from common.models import Tag


class TagBaseSerializer(serializers.ModelSerializer):
    """Serializer for tags used to C-R-U-Detail operations."""

    self = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Tag
        fields = [
            "self",
            "name",
        ]
        print(fields)

    def get_self(self, obj):
        """Get self_url property"""
        return obj.self_url

    def validate_name(self, value):
        """Validate that doesn't exists a tag with the same name for the current user"""
        user = self.context["request"].user
        if not Tag.objects.filter(user=user, name=value).exists():
            return value
        raise serializers.ValidationError("Ya tenes registrado un tag con ese nombre")


class TagNestedCUDSerializer(TagBaseSerializer):
    """Serializer for tags used to nested CUD operations."""

    def validate_name(self, value):
        """As this serializer is used to CUD nested operations, e.g. when creating a recipe,
        it's not necessary to check that the user already have a tag with the name, because
        that validations is made in the recipemodelserializer when call to his method _get_or_create_tags"""
        return value


class TagListedSerializer(TagBaseSerializer):
    """Serializer for tag list operation."""

    links = serializers.SerializerMethodField(read_only=True)

    class Meta(TagBaseSerializer.Meta):
        fields = TagBaseSerializer.Meta.fields + [
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


# Tag Serialization Aliases:
## Alias for retrieve operation
TagDetailedSerializer = TagListedSerializer
## Alias for nested serialization
TagRelatedSerializer = TagBaseSerializer
