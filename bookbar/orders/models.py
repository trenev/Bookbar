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
    DISCOUNT_WHEN_MORE_THAN_ONE_BOOK = 10
    MIN_BOOKS_COUNT_TO_APPLY_DISCOUNT = 2

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

    def get_books_count(self):
        return sum([b.quantity for b in self.books.all()])

    def get_discount(self):
        result = 0
        if self.get_books_count() >= self.MIN_BOOKS_COUNT_TO_APPLY_DISCOUNT:
            result = self.get_total_price() * self.DISCOUNT_WHEN_MORE_THAN_ONE_BOOK / 100
        return result

    def get_final_price(self):
        return self.get_total_price() - self.get_discount()
