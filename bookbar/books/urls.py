from django.urls import path

from bookbar.books.views import BookDetailView, EditBookView, DeleteBookView, AddBookView, BooksView

urlpatterns = (
    path('category/<str:category>/', BooksView.as_view(), name='show books'),
    path('details/<int:pk>/', BookDetailView.as_view(), name='book details'),

    path('add-book/', AddBookView.as_view(), name='add book'),
    path('edit-book/<int:pk>/', EditBookView.as_view(), name='edit book'),
    path('delete-book/<int:pk>/', DeleteBookView.as_view(), name='delete book'),
)
