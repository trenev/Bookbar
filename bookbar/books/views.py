from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from bookbar.books.forms import CreateBookForm, EditBookForm
from bookbar.books.models import Book, Category
from bookbar.common.mixins import UserPermissionMixin


class IndexView(views.ListView):
    template_name = 'common/index.html'
    model = Book
    queryset = Book.objects.all()[:5]


class BooksView(views.ListView):
    template_name = 'books/books.html'
    model = Book
    paginate_by = 8

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['category_list'] = Category.objects.all()
        data['category'] = self.kwargs.get('category')
        return data

    def get_queryset(self):
        category = self.kwargs.get('category')
        if category == 'all':
            return Book.objects.all()

        return Book.objects.filter(category__category_name__iexact=self.kwargs.get('category'))


class BookDetailView(views.DetailView):
    template_name = 'books/book_details.html'
    model = Book

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['annotation'] = self.object.annotation.split('\n')
        return data


class AddBookView(UserPermissionMixin, views.CreateView):
    permission_required = 'books.add_book'

    template_name = 'books/add_book.html'
    model = Book
    form_class = CreateBookForm
    success_url = reverse_lazy('index')


class EditBookView(UserPermissionMixin, views.UpdateView):
    permission_required = 'books.change_book'

    template_name = 'books/edit_book.html'
    model = Book
    form_class = EditBookForm

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('book details', kwargs={'pk': pk})


class DeleteBookView(UserPermissionMixin, views.DeleteView):
    permission_required = 'books.delete_book'

    template_name = 'books/delete_book.html'
    model = Book
    success_url = reverse_lazy('index')


def page_not_found_view(request, exception):
    return render(request, 'common/404.html', status=404)
