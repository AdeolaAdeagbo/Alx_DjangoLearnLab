from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    
    Handles serialization/deserialization of Book instances to/from JSON.
    Includes custom validation for publication_year.
    """
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
    
    def validate_publication_year(self, value):
        """
        Custom validation: Ensure publication year is not in the future.
        
        Args:
            value (int): The publication year to validate
        
        Returns:
            int: The validated publication year
        
        Raises:
            serializers.ValidationError: If year is in the future
        """
        current_year = datetime.now().year
        
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future. Current year is {current_year}."
            )
        
        if value < 1000:
            raise serializers.ValidationError(
                "Publication year must be a valid year (1000 or later)."
            )
        
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model with nested Book serialization.
    
    This serializer demonstrates a one-to-many relationship:
    - Each Author can have multiple Books
    - Books are nested within the Author's JSON representation
    
    The 'books' field uses BookSerializer to serialize all related books.
    The 'many=True' parameter indicates this is a list of books.
    The 'read_only=True' means books are only shown in GET requests,
    not accepted in POST/PUT requests.
    
    Example JSON output:
    {
        "id": 1,
        "name": "J.K. Rowling",
        "books": [
            {
                "id": 1,
                "title": "Harry Potter and the Philosopher's Stone",
                "publication_year": 1997,
                "author": 1
            },
            {
                "id": 2,
                "title": "Harry Potter and the Chamber of Secrets",
                "publication_year": 1998,
                "author": 1
            }
        ]
    }
    """
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']