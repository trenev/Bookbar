from datetime import date

from django.test import TestCase
from django.urls import reverse

from bookbar.books.models import Book, Category


class BooksViewTest(TestCase):
    VALID_CATEGORY = {
        'category_name': 'some category',
    }

    VALID_BOOK_DATA = {
        'title': 'title',
        'author': 'author',
        'annotation': 'annotation',
        'cover_image': 'zaq.jpg',
        'quantity': 1,
        'price': 5,
        'date_added': date.today(),
    }

    def test_books__when_no_specific_category(self):
        category = Category.objects.create(**self.VALID_CATEGORY)
        book = Book.objects.create(
            **self.VALID_BOOK_DATA,
            category=category,
        )
        response = self.client.get(reverse('show books', kwargs={
            'category': 'all',
        }))
        self.assertTemplateUsed(response, 'books/books.html')

