"""
Tests for ingredients APIs.
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from api.serializers.ingredient_serializers import IngredientListedSerializer
from common.models import Ingredient

INGREDIENTS_URL = reverse("api:ingredients-list")


def detail_url(ingredient_id):
    """Create and return an ingredient detail URL."""
    return reverse("api:ingredients-detail", args=[ingredient_id])


def create_ingredient(user, **params):
    """Create and return a sample recipe"""

    defaults = {
        "name": "Sample ingredient name",
    }

    defaults.update(params)

    ingredient = Ingredient.objects.create(
        user=user,
        **defaults,
    )

    return ingredient


def create_user(
    email="user@example.com",
    password="testpass123",
):
    """Create and return a new user"""
    return get_user_model().objects.create_user(email, password)


class PublicIngredientsAPITest(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API."""
        res = self.client.get(INGREDIENTS_URL)

        self.assertEqual(
            res.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )


class PrivateIngredientsAPITest(TestCase):
    """Test authenticated API requests"""

    def setUp(self):
        self.user = create_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_ingredients(self):
        """Test retrieving a list of ingredients"""
        Ingredient.objects.create(user=self.user, name="Cheese")
        Ingredient.objects.create(user=self.user, name="Ketchup")

        res = self.client.get(INGREDIENTS_URL)

        ingredients = Ingredient.objects.all().order_by("-name")
        serializer = IngredientListedSerializer(ingredients, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_ingredients_limited_to_user(self):
        """Test list of ingredients is to authenticated user"""
        user2 = create_user(
            email="user2@example.com",
        )

        Ingredient.objects.create(user=user2, name="Lemon")
        ingredient = Ingredient.objects.create(user=self.user, name="Cheese")

        res = self.client.get(INGREDIENTS_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]["name"], ingredient.name)

    def test_update_ingredient(self):
        """Test updating an ingredient."""
        ingredient = Ingredient.objects.create(user=self.user, name="Cilantro")
        payload = {
            "name": "Coriander",
        }
        url = detail_url(ingredient.id)
        res = self.client.patch(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        ingredient.refresh_from_db()
        self.assertEqual(ingredient.name, payload["name"])

    def test_delete_ingredient(self):
        """Test deleting a ingredient"""
        ingredient = Ingredient.objects.create(user=self.user, name="Lettuce")
        url = detail_url(ingredient.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        ingredients = Ingredient.objects.filter(user=self.user)
        self.assertFalse(ingredients.exists())
