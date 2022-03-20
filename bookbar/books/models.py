from django.db import models

from bookbar.common.validators import MaxFileSizeInMBValidator
from bookbar.common.models import SoftDeletionModel


class Category(SoftDeletionModel):
    CATEGORY_NAME_MAX_LENGTH = 30

    category_name = models.CharField(
        max_length=CATEGORY_NAME_MAX_LENGTH,
    )

    def __str__(self):
        return f'{self.category_name}'


class Book(SoftDeletionModel):
    TITLE_MAX_LENGTH = 50
    AUTHOR_MAX_LENGTH = 50

    IMAGE_UPLOAD_TO_DIR = 'images/'
    IMAGE_MAX_SIZE_IN_MB = 1

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    author = models.CharField(
        max_length=AUTHOR_MAX_LENGTH,
    )

    description = models.TextField()

    cover_image = models.ImageField(
        validators=(
            MaxFileSizeInMBValidator(IMAGE_MAX_SIZE_IN_MB),
        ),
        upload_to=IMAGE_UPLOAD_TO_DIR,
    )

    quantity = models.IntegerField()

    price = models.FloatField()

    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['-date_added']
