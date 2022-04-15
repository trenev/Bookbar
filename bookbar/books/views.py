from django.urls import reverse_lazy, reverse
from django.views import generic as views

from bookbar.books.forms import CreateBookForm, EditBookForm
from bookbar.books.models import Book, Category


class IndexView(views.ListView):
    template_name = 'common/index.html'
    model = Book
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['categories'] = Category.objects.all()
        return data

class BookDetailView(views.DetailView):
    template_name = 'books/book_details.html'
    model = Book


class AddBookView(views.CreateView):
    template_name = 'books/add_book.html'
    model = Book
    form_class = CreateBookForm
    success_url = reverse_lazy('index')


class EditBookView(views.UpdateView):
    template_name = 'books/edit_book.html'
    model = Book
    form_class = EditBookForm

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('book details', kwargs={'pk': pk})


class DeleteBookView(views.DeleteView):
    template_name = 'books/delete_book.html'
    model = Book
    success_url = reverse_lazy('index')

