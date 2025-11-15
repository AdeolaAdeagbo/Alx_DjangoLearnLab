from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """View books - requires can_view permission."""
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    """Create book - requires can_create permission."""
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            publication_year=request.POST['publication_year']
        )
    return render(request, 'bookshelf/form_example.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    """Edit book - requires can_edit permission."""
    return render(request, 'bookshelf/form_example.html')

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    """Delete book - requires can_delete permission."""
    return render(request, 'bookshelf/form_example.html')