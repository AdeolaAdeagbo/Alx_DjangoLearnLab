from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
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
    permission_classes = [IsAuthenticatedOrReadOnly]  # Add this


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for performing CRUD operations on Book model.
    Requires authentication for create, update, delete.
    Anyone can read.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Add this