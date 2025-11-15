from .models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "Author One"
author = Author.objects.get(name=author_name)
author_books = author.book_set.all()
print(author_books)

# List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
library_books = library.books.all()
print(library_books)

# Retrieve the librarian for a library
librarian = library.librarian
print(librarian)
