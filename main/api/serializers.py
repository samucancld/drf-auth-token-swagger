"""
Serializers for the API
"""

from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user model."""

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "password",
        )
        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 6
            }
        }

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
