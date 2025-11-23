from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Keep the existing BookList view
class BookList(generics.ListAPIView):
    """
    API endpoint that allows books to be viewed as a list.
    GET /api/books/ - Returns list of all books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Add this new ViewSet
class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for performing CRUD operations on Book model.
    
    Provides:
    - list: GET /api/books_all/
    - create: POST /api/books_all/
    - retrieve: GET /api/books_all/{id}/
    - update: PUT /api/books_all/{id}/
    - partial_update: PATCH /api/books_all/{id}/
    - destroy: DELETE /api/books_all/{id}/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer