from .models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.first()
print(author.book_set.all())

# List all books in a library
library = Library.objects.first()
print(library.books.all())

# Retrieve the librarian for a library
print(library.librarian)
