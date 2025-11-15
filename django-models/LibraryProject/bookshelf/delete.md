# Delete Operation

## Command
```python
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")

book.delete()

# Confirm deletion by checking if any books exist
all_books = Book.objects.all()
print(f"Number of books: {all_books.count()}")
print(f"Books: {list(all_books)}")
```

## Output
```
(1, {'bookshelf.Book': 1})
Number of books: 0
Books: []
```

Successfully deleted the book "Nineteen Eighty-Four". Confirmation shows 0 books remaining in the database.