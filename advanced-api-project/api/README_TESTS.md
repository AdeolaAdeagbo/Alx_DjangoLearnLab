# API Testing Documentation

## Running Tests

### Run All Tests
```bash
python manage.py test api
```

### Run with Verbose Output
```bash
python manage.py test api --verbosity=2
```

### Run Specific Test Class
```bash
python manage.py test api.test_views.BookAPITestCase
```

## Test Coverage

### BookAPITestCase
- `test_list_books`: Verifies GET /api/books/ returns all books
- `test_get_single_book`: Verifies GET /api/books/<id>/ returns correct book
- `test_create_book_authenticated`: Verifies authenticated users can create books
- `test_create_book_unauthenticated`: Verifies unauthenticated users cannot create
- `test_create_book_invalid_year`: Verifies validation rejects future years
- `test_update_book`: Verifies PUT updates work correctly
- `test_partial_update_book`: Verifies PATCH allows partial updates
- `test_delete_book`: Verifies DELETE removes books
- `test_filter_by_author`: Verifies filtering by author works
- `test_filter_by_year`: Verifies filtering by year works
- `test_search_by_title`: Verifies search functionality
- `test_ordering_by_year`: Verifies ordering functionality

### AuthorAPITestCase
- `test_list_authors`: Verifies authors list with nested books
- `test_get_author_detail`: Verifies single author detail view

## Test Data
Tests use isolated test database. Original data is not affected.