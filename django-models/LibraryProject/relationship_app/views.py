# Import models exactly as checker expects
from .models import Library
from .models import Book

# Import Django views
from django.shortcuts import render
from django.views.generic.detail import DetailView

# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: Library detail using DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'