# Update Operation

## Command
```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")

book.title = "Nineteen Eighty-Four"
book.save()

print(f"Updated Title: {book.title}")
```

## Output
```
Updated Title: Nineteen Eighty-Four
```

Successfully updated the book title from "1984" to "Nineteen Eighty-Four".