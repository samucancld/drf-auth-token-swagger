"""
API URL configuration
"""

from django.urls import include, path

from . import routers, views

# Resources:
USERS = "users"
RECIPES = "recipes"

app_name = "api"
urlpatterns = [
    path(f"{USERS}/me", views.RetrieveUpdateUserView.as_view(), name="me"),
    path(f"{USERS}/token", views.RetrieveCreateTokenView.as_view(), name="token"),
    path(f"{USERS}/register", views.CreateUserView.as_view(), name="create"),
    path(f"{USERS}/list", views.ListUserView.as_view(), name="create"),
    path("", include(routers)),
]


print(urlpatterns)
