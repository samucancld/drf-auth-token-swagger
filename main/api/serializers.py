"""
Serializers for the API
"""

from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from common.models import Recipe, Tag


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user model."""

    self = serializers.SerializerMethodField(
        read_only = True
    )

    links = serializers.SerializerMethodField(
        read_only = True
    )

    class Meta:
        model = get_user_model()
        fields = (
            "self",
            "username",
            "password",
            "links",
        )
        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 6
            }
        }

    def get_links(self, obj):
        links = []
        for recipe in obj.recipes.all():
            link = {
                "rel": "recipe",
                "href": recipe.self_url,
            }
            links.append(link)
        return links

    def get_self(self, obj):
        return obj.self_url

    def create(self, validated_data):
        """Create and return a user with encrypted pssword
        The default behavior of the ModelSerializer is using the objects.create() method,
        wich doesn't work on this because an extra step is needed (hashing pwd) and this
        is defined in the custom manager for the user."""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

class TokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""

    username = serializers.CharField()
    password = serializers.CharField(
        style={
            "input_type": "password",
        },
        trim_whitespace=False,
    )

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        user = authenticate(
            request=self.context.get("request"),
            username=username,
            password=password,
        )
        if not user:
            msg = _("Unable to authenticate with provided credentials.")
            raise serializers.ValidationError(msg, code="authorization")
        attrs["user"] = user
        return attrs

class TagBaseSerializer(serializers.ModelSerializer):
    """Serializer for tags used to C-R-U-Detail operations."""

    self = serializers.SerializerMethodField(
        read_only = True
    )

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
        user = self.context['request'].user
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

    links = serializers.SerializerMethodField(
        read_only = True
    )

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

class RecipeBaseSerializer(serializers.ModelSerializer):
    """Base serializer for recipes. Contains all model fields plus self property
    and avoid id representation and description."""

    self = serializers.SerializerMethodField(read_only = True)

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

    class Meta(RecipeBaseSerializer.Meta):
        fields = RecipeBaseSerializer.Meta.fields + [
            "description",
            "tags",
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

    def create(self, validated_data):
        """Creaste a recipe."""
        tags = validated_data.pop("tags", [])
        recipe = Recipe.objects.create(**validated_data)
        self._get_or_create_tags(tags, recipe)

        return recipe

    def update(self, instance, validated_data):
        """Update a recipe"""
        tags = validated_data.pop("tags", None)
        if tags is not None:
            instance.tags.clear()
            self._get_or_create_tags(tags, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    def validate_title(self, value):
        """
        As this recipe model serializers is used to CUD operations, is it necessary
        to validate that doesn't exist a recipe with the same title for the current user
        """
        user = self.context['request'].user
        if not Recipe.objects.filter(user=user, title=value).exists():
            return value
        raise serializers.ValidationError("Ya tenes registrada una receta con ese nombre")

class RecipeListedSerializer(RecipeBaseSerializer):
    """
    Serializer for list operation for the recipe, just add links field to the
    base recipe serializer
    """

    links = serializers.SerializerMethodField(read_only = True)

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
        return links

class RecipeDetailedSerializer(RecipeBaseSerializer):
    """
    Serializer for recipe detail view. Just add nested tag serializer
    """

    tags = TagRelatedSerializer(
        many = True,
    )

    class Meta(RecipeBaseSerializer.Meta):
        fields = RecipeBaseSerializer.Meta.fields + [
            "description",
            "tags",
        ]

class RecipeRelatedSerializer(RecipeBaseSerializer):
    pass