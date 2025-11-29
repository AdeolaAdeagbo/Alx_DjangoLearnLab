from django.db import models
from datetime import datetime

class Author(models.Model):
    """
    Author model representing a book author.
    
    Fields:
        name (str): The full name of the author
    
    Relationships:
        books (reverse ForeignKey): All books written by this author
    """
    name = models.CharField(max_length=200, help_text="Author's full name")
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Book(models.Model):
    """
    Book model representing a published book.
    
    Fields:
        title (str): The title of the book
        publication_year (int): Year the book was published
        author (ForeignKey): Reference to the Author who wrote this book
    
    Relationships:
        author (ForeignKey to Author): Many-to-one relationship
            - Each book has one author
            - Each author can have multiple books
            - Uses 'related_name' to access books from Author: author.books.all()
    """
    title = models.CharField(max_length=200, help_text="Book title")
    publication_year = models.IntegerField(help_text="Year published")
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        help_text="Author of this book"
    )
    
    def __str__(self):
        return f"{self.title} ({self.publication_year})"
    
    class Meta:
        ordering = ['-publication_year', 'title']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'