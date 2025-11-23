from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Converts Book instances to JSON and vice versa.
    """
    
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields
        # Or specify fields: fields = ['id', 'title', 'author', 'publication_year', 'isbn']