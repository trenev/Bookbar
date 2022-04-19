from django import template

from bookbar.orders.models import Order

register = template.Library()


@register.filter(name='count')
def order_books_count(user):
    ordered_books = Order.objects.filter(customer=user, ordered=False)
    if ordered_books.exists():
        return ordered_books[0].get_books_count()
    return 0
