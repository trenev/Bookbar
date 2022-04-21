from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

from bookbar.auth_app.models import AppUser
from bookbar.common.validators import validate_only_letters
from bookbar.common.models import SoftDeletionModel

UserModel = get_user_model()


class Profile(SoftDeletionModel):
    FIRST_NAME_MAX_LENGTH = 20
    LAST_NAME_MAX_LENGTH = 20

    PHONE_NUMBER_DIGIT_COUNT = 16
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
        max_length=PHONE_NUMBER_DIGIT_COUNT,
        unique=True,
        null=True,
        blank=True,
        validators=[PHONE_NUMBER_REGEX],
    )

    is_complete = models.BooleanField(
        default=False,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

