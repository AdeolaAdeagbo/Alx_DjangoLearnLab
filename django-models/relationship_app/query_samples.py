from .models import Author, Book, Library, Librarian

# ----- Setup sample data -----
# Only needed if your database is empty, you can comment these out if you already have data
author1, _ = Author.objects.get_or_create(name="Author One")
author2, _ = Author.objects.get_or_create(name="Author Two")

book1, _ = Book.objects.get_or_create(title="Book One", author=author1)
book2, _ = Book.objects.get_or_create(title="Book Two", author=author1)
book3, _ = Book.objects.get_or_create(title="Book Three", author=author2)

library1, _ = Library.objects.get_or_create(name="Central Library")
library1.books.set([book1, book3])  # assign some books
library2, _ = Library.objects.get_or_create(name="Community Library")
library2.books.set([book2])

librarian1, _ = Librarian.objects.get_or_create(name="Librarian A", library=library1)
librarian2, _ = Librarian.objects.get_or_create(name="Librarian B", library=library2)

# ----- Queries required by ALX checker -----

# 1. Query all books by a specific author (checker expects author_name)
author_name = "Author One"
author = Author.objects.get(name=author_name)
print(author.book_set.all())

# 2. List all books in a library (checker expects library_name)
library_name = "Central Library"
library = Library.objects.get(name=library_name)
print(library.books.all())

# 3. Retrieve the librarian for a library
print(library.librarian)
