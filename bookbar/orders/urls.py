from django.urls import path

from bookbar.orders.views import add_to_cart, OrderDetailsView, RemoveSingleItemFromCartView, \
    RemoveFromCartView, FinishOrderView, AddItemFromCartView

urlpatterns = (
    path('add-from-books/<int:pk>/', add_to_cart, name='add to cart'),
    path('add-from-cart/<int:pk>/', AddItemFromCartView.as_view(), name='increase added item to cart'),
    path('remove-from-cart/<int:pk>/', RemoveFromCartView.as_view(), name='remove from cart'),
    path('remove-item-from-cart/<int:pk>/', RemoveSingleItemFromCartView.as_view(), name='remove single item from cart'),
    path('details/<int:pk>/', OrderDetailsView.as_view(), name='order details'),
    path('finish/<int:pk>/', FinishOrderView.as_view(), name='finish order'),
)
