from django.contrib import messages
from django.contrib.auth import mixins
from django.contrib.auth.decorators import login_required
from django.core import exceptions
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import generic as views

from bookbar.books.models import Book
from bookbar.orders.models import OrderBook, Order


class OrderDetailsView(mixins.LoginRequiredMixin, views.View):
    def get(self, request, *args, **kwargs):
        try:
            order = Order.objects.get(customer=self.request.user, ordered=False)
            ordered_books = OrderBook.objects.filter(customer_id=self.request.user, ordered=False)

            context = {
                'order': order,
                'ordered_books': ordered_books,
            }

            return render(self.request, 'orders/cart.html', context)

        except exceptions.ObjectDoesNotExist:
            messages.warning(self.request, 'Your Cart is empty')
            return redirect('index')


@login_required
def add_to_cart(request, pk):
    book = get_object_or_404(Book, pk=pk)
    order_book, created = OrderBook.objects.get_or_create(
        customer=request.user,
        book=book,
        ordered=False,
    )

    book.quantity -= 1
    book.save()
    order_query_set = Order.objects.filter(customer=request.user, ordered=False)

    if order_query_set.exists():
        order = order_query_set[0]
        if order.books.filter(book__pk=book.pk).exists():
            order_book.quantity += 1
            order_book.save()
            return redirect('show books', category='all')
        else:
            order.books.add(order_book)
            return redirect('show books', category='all')

    else:
        order_date = timezone.now()
        order = Order.objects.create(
            customer=request.user,
            order_date=order_date,
        )
        order.books.add(order_book)
        return redirect('show books', category='all')


@login_required
def remove_from_cart(request, pk):
    order = Order.objects.get(customer=request.user, ordered=False)
    ordered_book = OrderBook.objects.get(pk=pk)

    book = Book.objects.get(pk=ordered_book.book.pk)
    qty = ordered_book.quantity
    book.quantity += qty
    book.save()

    ordered_book.delete()
    if order.books.all():
        return redirect('order details', pk=order.pk)
    else:
        order.delete()
        return redirect('index')


def finish_order(request, pk):
    order = Order.objects.get(pk=pk)
    ordered_books = OrderBook.objects.filter(order=order)

    order.ordered = True
    order.save()

    for book in ordered_books:
        book.ordered = True
        book.save()
    messages.success(request, 'Your order has been finished successfully.')

    return redirect('index')
