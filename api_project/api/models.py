from django.db import models

class Book(models.Model):
    """
    Book model for the API
    """
    title = models.CharField(max_length=200, help_text="Book title")
    author = models.CharField(max_length=100, help_text="Book author")
    publication_year = models.IntegerField(null=True, blank=True, help_text="Year published")
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True, help_text="ISBN number")
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    class Meta:
        ordering = ['title']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'