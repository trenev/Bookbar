from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import exceptions
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import generic as views

from bookbar.books.models import Book
from bookbar.common.mixins import UserAccessMixin, OrderedBookAccessMixin, OrderAccessMixin
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


class RemoveFromCartView(OrderedBookAccessMixin, views.View):
    def get(self, request, *args, **kwargs):
        order = Order.objects.get(customer=self.request.user, ordered=False)
        ordered_book = get_object_or_404(OrderBook, pk=self.kwargs['pk'])
        book = Book.objects.get(pk=ordered_book.book.pk)

        qty = ordered_book.quantity
        book.quantity += qty
        book.save()

        ordered_book.delete()

        if not order.books.all():
            order.delete()
            return redirect('index')

        messages.info(request, 'This book was removed from your cart.')
        return redirect('order details', pk=order.customer_id)


class RemoveSingleItemFromCartView(OrderedBookAccessMixin, views.View):
    def get(self, request, *args, **kwargs):
        order = Order.objects.get(customer=self.request.user, ordered=False)
        ordered_book = OrderBook.objects.get(pk=self.kwargs['pk'])
        book = Book.objects.get(pk=ordered_book.book.pk)

        book.quantity += 1
        book.save()

        if ordered_book.quantity > 1:
            ordered_book.quantity -= 1
            ordered_book.save()
        else:
            ordered_book.delete()

        if not order.books.all():
            order.delete()
            return redirect('index')

        messages.info(request, 'Book quantity was updated.')
        return redirect('order details', pk=order.customer_id)


class FinishOrderView(OrderAccessMixin, views.View):
    def get(self, request, *args, **kwargs):
        order = Order.objects.get(pk=self.kwargs['pk'])
        ordered_books = OrderBook.objects.filter(order=order)

        order.ordered = True
        order.save()

        for book in ordered_books:
            book.ordered = True
            book.save()
        messages.success(request, 'Your order has been finished successfully.')

        return redirect('index')


class AddItemFromCartView(OrderedBookAccessMixin, views.View):
    def get(self, request, *args, **kwargs):
        order = Order.objects.get(customer=self.request.user, ordered=False)
        ordered_book = OrderBook.objects.get(pk=self.kwargs['pk'])
        book = Book.objects.get(pk=ordered_book.book.pk)

        book.quantity -= 1
        book.save()

        ordered_book.quantity += 1
        ordered_book.save()

        messages.info(request, 'Book quantity was updated.')
        return redirect('order details', pk=order.customer_id)


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
            messages.info(request, 'Book quantity was updated.')
            return redirect('show books', category='all')
        else:
            order.books.add(order_book)
            messages.info(request, 'Book was added to your cart')
            return redirect('show books', category='all')

    else:
        order_date = timezone.now()
        order = Order.objects.create(
            customer=request.user,
            order_date=order_date,
        )
        order.books.add(order_book)
        messages.info(request, 'Book was added to your cart')
        return redirect('show books', category='all')

