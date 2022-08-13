"""
API URL configuration
"""

from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "api"
urlpatterns = [
    path('users/me', views.RetrieveUpdateUserView.as_view(), name='me'),
    path('users/token', views.RetrieveCreateTokenView.as_view(), name='token'),
    path("users/register", views.CreateUserView.as_view(), name="create"),
    path("users/list", views.ListUserView.as_view(), name="create"),
]
