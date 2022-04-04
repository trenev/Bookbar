from django.contrib.auth import get_user_model
from django.db import models

from bookbar.books.models import Book

UserModel = get_user_model()


class OrderBook(models.Model):
    quantity = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=1,
    )

    ordered = models.BooleanField(
        default=False,
    )

    customer = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )

    def get_price(self):
        return self.quantity * self.book.price

    def __str__(self):
        return f'{self.book.title}'


class Order(models.Model):
    order_date = models.DateTimeField(
        auto_now_add=True,
    )

    ordered = models.BooleanField(
        default=False,
    )

    customer = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    books = models.ManyToManyField(
        OrderBook,
    )

    def get_total_price(self):
        result = 0
        for book in self.books.all():
            result += book.get_price()
        return result

