# from datetime import date
#
# from django.test import TestCase
# from django.urls import reverse
#
# from bookbar.books.models import Book, Category
#
#
# class BookDetailViewTest(TestCase):
#     VALID_CATEGORY = {
#         'category_name': 'Some category',
#     }
#
#     VALID_BOOK_DATA = {
#         'title': 'title',
#         'author': 'author',
#         'annotation': 'annotation',
#         'cover_image': 'zaq.jpg',
#         'quantity': 1,
#         'price': 5,
#         'date_added': date.today(),
#     }
#
#     def test_book_details(self):
#         category = Category.objects.create(**self.VALID_CATEGORY)
#         book = Book.objects.create(
#             **self.VALID_BOOK_DATA,
#             category=category,
#         )
#         book.save()
#         response = self.client.get(reverse('book details', kwargs={
#             'pk': 1,
#         }))
#         self.assertTemplateUsed(response, 'books/book_details.html')
