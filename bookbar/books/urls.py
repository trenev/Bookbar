from django.urls import path

from bookbar.books.views import BookDetailView, EditBookView

urlpatterns = (
    path('details/<int:pk>/', BookDetailView.as_view(), name='book details'),
    path('edit-book/<int:pk>/', EditBookView.as_view(), name='edit book'),
)
