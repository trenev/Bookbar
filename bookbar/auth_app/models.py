from django.contrib.auth import models as auth_models
from django.db import models

from bookbar.common.managers import AppUsersManager
from bookbar.common.models import SoftDeletionModel


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin, SoftDeletionModel):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = AppUsersManager()

