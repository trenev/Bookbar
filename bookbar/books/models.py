from cloudinary import models as cloudinary_models
from django.core.validators import MinValueValidator
from django.db import models

from bookbar.common.models import SoftDeletionModel


class Category(SoftDeletionModel):
    CATEGORY_NAME_MAX_LENGTH = 30

    category_name = models.CharField(
        max_length=CATEGORY_NAME_MAX_LENGTH,
    )

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return f'{self.category_name}'


class Book(SoftDeletionModel):
    TITLE_MAX_LENGTH = 150
    AUTHOR_MAX_LENGTH = 50

    IMAGE_UPLOAD_TO_DIR = 'images/'

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    author = models.CharField(
        max_length=AUTHOR_MAX_LENGTH,
    )

    annotation = models.TextField()

    cover_image = cloudinary_models.CloudinaryField('image')

    quantity = models.IntegerField(
        validators=[MinValueValidator(1)],
    )

    price = models.FloatField(
        validators=[MinValueValidator(0)],
    )

    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f'{self.title}'

