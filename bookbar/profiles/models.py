from django.core.validators import RegexValidator
from django.db import models

from bookbar.auth_app.models import AppUser
from bookbar.books.validators import validate_only_letters
from bookbar.orders.models import SoftDeletionModel


class Profile(SoftDeletionModel):
    FIRST_NAME_MAX_LENGTH = 20
    LAST_NAME_MAX_LENGTH = 20

    PHONE_NUMBER_REGEX = RegexValidator(
        regex=r'^(\+\d{1,3})?,?\s?\d{8,13}',
        message='Phone number must not consist of space and requires country code. eg: +6591258565'
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
        validators=(
            validate_only_letters,
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
        validators=(
            validate_only_letters,
        ),
    )

    phone_number = models.CharField(
        max_length=16,
        unique=True,
        null=True,
        blank=True,
        validators=[PHONE_NUMBER_REGEX],
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

