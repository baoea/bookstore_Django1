from books.models import Book
from django.contrib import admin
from django.contrib.admin import ModelAdmin


class BookAdmin(ModelAdmin):
    list_display = ("id", "title", "category", "author", "publishedDate", "created_at", "updated_at")


admin.site.register(Book, BookAdmin)
