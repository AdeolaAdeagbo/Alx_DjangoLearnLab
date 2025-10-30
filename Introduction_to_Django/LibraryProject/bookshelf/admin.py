from django.contrib import admin
from .models import Book

# Register the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # shows these columns in admin list view
    list_filter = ('author', 'publication_year')  # allows filtering
    search_fields = ('title', 'author')  # adds a search bar

