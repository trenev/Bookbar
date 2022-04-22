from django.contrib import messages
from django.contrib.auth import mixins
from django.contrib.auth.decorators import login_required
from django.core import exceptions
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import generic as views

from bookbar.books.models import Book
from bookbar.common.mixins import UserAccessMixin
from bookbar.orders.models import OrderBook, Order
from bookbar.profiles.models import Profile


class OrderDetailsView(UserAccessMixin, views.View):
    def get(self, request, *args, **kwargs):
        try:
            profile = Profile.objects.get(pk=self.request.user.pk)
            order = Order.objects.get(customer=self.request.user, ordered=False)
            ordered_books = OrderBook.objects\
                .filter(customer_id=self.request.user, ordered=False)\
                .order_by('book__title')

            context = {
                'profile': profile,
                'order': order,
                'ordered_books': ordered_books,
            }

            if not profile.is_complete:
                messages.warning(self.request, 'You need to complete your profile before finishing the order.')

            return render(self.request, 'orders/cart.html', context)

        except exceptions.ObjectDoesNotExist:
            messages.warning(self.request, 'Your Cart is empty')
            return redirect('index')


class FinishOrderView(mixins.LoginRequiredMixin, views.View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.pk == self.kwargs['pk']:
            return render(request, 'common/404.html')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        order = get_object_or_404(Order, pk=self.kwargs['pk'])
        ordered_books = OrderBook.objects.filter(order=order)

        order.ordered = True
        order.save()

        for book in ordered_books:
            book.ordered = True
            book.save()

        messages.success(request, 'Your order has been finished successfully.')
        return redirect('index')
    

@login_required
def add_to_cart(request, pk):
    book_is_ordered = False
    book = get_object_or_404(Book, pk=pk)

    order_query_set = Order.objects.filter(customer=request.user, ordered=False)
    if order_query_set.exists():
        order = order_query_set[0]
    else:
        order_date = timezone.now()
        order = Order.objects.create(customer=request.user, order_date=order_date)

    order_book_query_set = OrderBook.objects.filter(customer=request.user, book=book, ordered=False)
    if order_book_query_set.exists():
        order_book = order_book_query_set[0]

        if book.quantity < 1:
            messages.info(request, 'The book is out of stock. It can not be added to your cart.')
            return redirect('show books', category='all')

        book.quantity -= 1
        order_book.quantity += 1
        book.save()
        order_book.save()
        book_is_ordered = True
    else:
        if book.quantity < 1:
            messages.info(request, 'The book is out of stock. It can not be added to your cart.')
            return redirect('show books', category='all')

        book.quantity -= 1
        order_book = OrderBook.objects.create(customer=request.user, book=book, ordered=False)
        order.books.add(order_book)
        book.save()

    if 'add-quantity-to-cart' in request.path:
        messages.info(request, 'Book quantity was updated.')
        return redirect('order details', pk=order.customer_id)

    if book_is_ordered:
        messages.info(request, 'Book quantity was updated.')
        return redirect('show books', category='all')
    else:
        messages.info(request, 'Book was added to your cart')
        return redirect('show books', category='all')


@login_required
def remove_quantity_from_cart(request, pk):
    book = get_object_or_404(Book, pk=pk)

    order_query_set = Order.objects.filter(customer=request.user, ordered=False)
    if order_query_set.exists():
        order = order_query_set[0]

        order_book_query_set = OrderBook.objects.filter(customer=request.user, book=book, ordered=False)
        if order_book_query_set.exists():
            order_book = order_book_query_set[0]
            if order_book.quantity > 1:
                order_book.quantity -= 1
                order_book.save()

            else:
                order.books.remove(order_book)
                order_book.delete()

            book.quantity += 1
            book.save()

        if not order.books.all():
            order.delete()
            messages.warning(request, 'Your Cart is empty')
            return redirect('index')

        messages.info(request, 'Book quantity was updated.')
        return redirect('order details', pk=order.customer_id)

    return redirect('index')


@login_required
def remove_from_cart(request, pk):
    book = get_object_or_404(Book, pk=pk)

    order_query_set = Order.objects.filter(customer=request.user, ordered=False)
    if order_query_set.exists():
        order = order_query_set[0]

        order_book_query_set = OrderBook.objects.filter(customer=request.user, book=book, ordered=False)
        if order_book_query_set.exists():
            order_book = order_book_query_set[0]
            order.books.remove(order_book)
            order_book.delete()

            book.quantity += order_book.quantity
            book.save()

        if not order.books.all():
            order.delete()
            messages.warning(request, 'Your Cart is empty')
            return redirect('index')

        messages.info(request, 'This book was removed from your cart.')
        return redirect('order details', pk=order.customer_id)

    return redirect('index')




