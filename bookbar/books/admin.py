from django.contrib import admin

from bookbar.books.models import Category, Book


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)


@admin.register(Book)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'quantity', 'price', 'category')
