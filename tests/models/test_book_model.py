from datetime import date

from django.core.exceptions import ValidationError
from django.test import TestCase

from bookbar.books.models import Category, Book


class BookModelTest(TestCase):
    VALID_CATEGORY = {
        'category_name': 'some category',
    }

    VALID_BOOK_DATA = {
        'title': 'some title',
        'author': 'some author',
        'annotation': 'some annotation',
        'cover_image': 'zaq.jpg',
        'date_added': date.today(),
    }

    def __create_category(self):
        return Category.objects.create(**self.VALID_CATEGORY)

    def test_book_model__when_data_is_correct__expect_success(self):
        category = self.__create_category()
        book = Book.objects.create(
            **self.VALID_BOOK_DATA,
            quantity=1,
            price=5,
            category=category,
        )

        self.assertEqual('some title', book.title)
        self.assertEqual('some author', book.author)
        self.assertEqual('some annotation', book.annotation)
        self.assertEqual('zaq.jpg', book.cover_image)
        self.assertEqual(1, book.quantity)
        self.assertEqual(5, book.price)
        self.assertEqual('some category', book.category.category_name)
        self.assertIsNotNone(book.date_added)

        book.full_clean()
        book.save()

    def test_book_model__when_quantity_is_0__expect_to_raise(self):
        category = self.__create_category()
        book = Book.objects.create(
            **self.VALID_BOOK_DATA,
            quantity=0,
            price=5,
            category=category,
        )
        with self.assertRaises(ValidationError) as context:
            book.full_clean()
            book.save()
        self.assertIsNotNone(context.exception)

    def test_book_model__when_price_is_less_than_0__expect_to_raise(self):
        category = self.__create_category()
        book = Book.objects.create(
            **self.VALID_BOOK_DATA,
            quantity=1,
            price=-1,
            category=category,
        )
        with self.assertRaises(ValidationError) as context:
            book.full_clean()
            book.save()
        self.assertIsNotNone(context.exception)
