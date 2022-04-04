from django.urls import path

from bookbar.orders.views import add_to_cart, OrderDetailsView, finish_order, remove_from_cart

urlpatterns = (
    path('add-to-cart/<int:pk>/', add_to_cart, name='add to cart'),
    path('remove-from-cart/<int:pk>/', remove_from_cart, name='remove from cart'),
    path('details/<int:pk>/', OrderDetailsView.as_view(), name='order details'),
    path('finish/<int:pk>/', finish_order, name='finish order'),
)
