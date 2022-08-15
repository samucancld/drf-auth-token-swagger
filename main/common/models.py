"""
Databse models.
"""

from django.conf import settings
from django.db import models #used for fields
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users"""
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given username, and password.
        """
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        """
        Creates and saves a superuser with the given username, and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system. Inherits from AbstractBaseUser wich only define the password field.
    Mixins: PermissionsMixin"""

    username = models.CharField(
        max_length = 255,
        unique = True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # All admins are staff
        return self.is_admin

    @property
    def self_url(self) -> str:
        return f"/api/users/me"

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

class Tag(models.Model):
    """Tag for filtering recipes"""

    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tags",
    )

    def __str__(self) -> str:
        return self.name

    @property
    def self_url(self) -> str:
        return f"/api/tags/{self.id}"

class Recipe(models.Model):
    """Recipe model."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = "recipes",
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    time_minutes = models.IntegerField()
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    tags = models.ManyToManyField(
        Tag,
        related_name="recipes",
    )

    @property
    def self_url(self) -> str:
        return f"/api/recipes/{self.id}"

    def __str__(self) -> str:
        return self.title
