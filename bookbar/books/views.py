from django.shortcuts import render
from django.views import generic as views

from bookbar.books.models import Book


class IndexView(views.ListView):
    model = Book
    template_name = 'common/index.html'


class BookDetailView(views.DetailView):
    model = Book
    template_name = 'books/book_details.html'


class EditBookView(views.UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'books/edit_book.html'
