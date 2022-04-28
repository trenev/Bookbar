from datetime import date

from django.test import TestCase
from django.urls import reverse

from bookbar.books.models import Book, Category


class IndexViewTest(TestCase):
    # VALID_CATEGORY = {
    #     'category_name': 'Some category',
    # }
    #
    # VALID_BOOK_DATA = {
    #     'title': 'title',
    #     'author': 'author',
    #     'annotation': 'annotation',
    #     'cover_image': 'zaq.jpg',
    #     'quantity': 1,
    #     'price': 5,
    #     'date_added': date.today(),
    # }

    def test_index__expect_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'common/index.html')
