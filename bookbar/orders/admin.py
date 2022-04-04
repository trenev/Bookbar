from django.contrib import admin

from bookbar.orders.models import Order, OrderBook


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_date', 'ordered')
    list_filter = ('ordered',)


@admin.register(OrderBook)
class OrderBookAdmin(admin.ModelAdmin):
    list_display = ('customer', 'book', 'quantity', 'ordered')
    list_filter = ('ordered',)
