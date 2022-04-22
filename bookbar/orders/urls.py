from django.urls import path

from bookbar.orders.views import add_to_cart, OrderDetailsView, FinishOrderView, remove_from_cart, \
    remove_quantity_from_cart

urlpatterns = (
    path('add-to_cart/<int:pk>/', add_to_cart, name='add to cart'),
    path('add-quantity-to-cart/<int:pk>/', add_to_cart, name='add quantity to cart'),
    path('remove-from-cart/<int:pk>/', remove_from_cart, name='remove from cart'),
    path('remove-quantity-from-cart/<int:pk>/', remove_quantity_from_cart, name='remove quantity from cart'),
    path('details/<int:pk>/', OrderDetailsView.as_view(), name='order details'),
    path('finish/<int:pk>/', FinishOrderView.as_view(), name='finish order'),
)
