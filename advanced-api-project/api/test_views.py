from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Author, Book
from datetime import datetime

class BookAPITestCase(APITestCase):
    """
    Comprehensive tests for Book API endpoints.
    Uses both Token authentication and client.login() methods.
    """
    
    def setUp(self):
        """
        Set up test data that will be used across multiple tests.
        Runs before each test method.
        
        Note: Django automatically uses a separate test database
        for running tests, so production/development data is not affected.
        """
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create auth token
        self.token = Token.objects.create(user=self.user)
        
        # Create test author
        self.author = Author.objects.create(name="Test Author")
        
        # Create test books
        self.book1 = Book.objects.create(
            title="Test Book 1",
            publication_year=2020,
            author=self.author
        )
        
        self.book2 = Book.objects.create(
            title="Test Book 2",
            publication_year=2021,
            author=self.author
        )
        
        # Set up API client
        self.client = APIClient()
    
    def test_list_books(self):
        """
        Test GET /api/books/
        Should return list of all books.
        """
        response = self.client.get('/api/books/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        self.assertEqual(len(response.data['results']), 2)
    
    def test_get_single_book(self):
        """
        Test GET /api/books/<id>/
        Should return single book details.
        """
        response = self.client.get(f'/api/books/{self.book1.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book 1')
        self.assertEqual(response.data['publication_year'], 2020)
    
    def test_create_book_authenticated(self):
        """
        Test POST /api/books/create/
        Authenticated user should be able to create a book.
        Uses Token authentication.
        """
        # Authenticate with token
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.id
        }
        
        response = self.client.post('/api/books/create/', data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Book')
        self.assertEqual(Book.objects.count(), 3)
    
    def test_create_book_with_login(self):
        """
        Test POST /api/books/create/
        Using client.login() for authentication.
        This demonstrates session-based authentication.
        """
        # Login using username and password
        login_success = self.client.login(username='testuser', password='testpass123')
        self.assertTrue(login_success, "Login should succeed")
        
        data = {
            'title': 'Book Created with Login',
            'publication_year': 2023,
            'author': self.author.id
        }
        
        response = self.client.post('/api/books/create/', data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Book Created with Login')
        
        # Logout after test
        self.client.logout()
    
    def test_create_book_unauthenticated(self):
        """
        Test POST /api/books/create/
        Unauthenticated user should NOT be able to create a book.
        """
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.id
        }
        
        response = self.client.post('/api/books/create/', data)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_create_book_invalid_year(self):
        """
        Test POST /api/books/create/
        Should reject books with future publication year.
        Tests custom validation in serializer.
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        
        future_year = datetime.now().year + 1
        data = {
            'title': 'Future Book',
            'publication_year': future_year,
            'author': self.author.id
        }
        
        response = self.client.post('/api/books/create/', data)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', response.data)
    
    def test_update_book(self):
        """
        Test PUT /api/books/<id>/update/
        Authenticated user should be able to update a book.
        Uses Token authentication.
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        
        data = {
            'title': 'Updated Title',
            'publication_year': 2022,
            'author': self.author.id
        }
        
        response = self.client.put(f'/api/books/{self.book1.id}/update/', data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Title')
        
        # Verify in database
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')
    
    def test_update_book_with_login(self):
        """
        Test PUT /api/books/<id>/update/
        Using client.login() for authentication.
        """
        # Login
        self.client.login(username='testuser', password='testpass123')
        
        data = {
            'title': 'Updated via Login',
            'publication_year': 2022,
            'author': self.author.id
        }
        
        response = self.client.put(f'/api/books/{self.book1.id}/update/', data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated via Login')
        
        self.client.logout()
    
    def test_partial_update_book(self):
        """
        Test PATCH /api/books/<id>/update/
        Should allow partial updates.
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        
        data = {'title': 'Partially Updated'}
        
        response = self.client.patch(f'/api/books/{self.book1.id}/update/', data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Partially Updated')
        # Year should remain unchanged
        self.assertEqual(response.data['publication_year'], 2020)
    
    def test_delete_book(self):
        """
        Test DELETE /api/books/<id>/delete/
        Authenticated user should be able to delete a book.
        Uses Token authentication.
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        
        initial_count = Book.objects.count()
        
        response = self.client.delete(f'/api/books/{self.book1.id}/delete/')
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), initial_count - 1)
    
    def test_delete_book_with_login(self):
        """
        Test DELETE /api/books/<id>/delete/
        Using client.login() for authentication.
        """
        # Login
        login_success = self.client.login(username='testuser', password='testpass123')
        self.assertTrue(login_success)
        
        response = self.client.delete(f'/api/books/{self.book2.id}/delete/')
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        self.client.logout()
    
    def test_filter_by_author(self):
        """
        Test filtering books by author.
        """
        response = self.client.get(f'/api/books/?author={self.author.id}')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
    
    def test_filter_by_year(self):
        """
        Test filtering books by publication year.
        """
        response = self.client.get('/api/books/?publication_year=2020')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Test Book 1')
    
    def test_search_by_title(self):
        """
        Test searching books by title.
        """
        response = self.client.get('/api/books/?search=Book 1')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Test Book 1')
    
    def test_ordering_by_year(self):
        """
        Test ordering books by publication year.
        """
        response = self.client.get('/api/books/?ordering=-publication_year')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # First result should be the newest (2021)
        self.assertEqual(response.data['results'][0]['publication_year'], 2021)


class AuthorAPITestCase(APITestCase):
    """
    Tests for Author API endpoints.
    Demonstrates testing nested serializers.
    """
    
    def setUp(self):
        """
        Set up test data.
        Uses separate test database automatically.
        """
        self.author = Author.objects.create(name="Test Author")
        
        self.book1 = Book.objects.create(
            title="Book 1",
            publication_year=2020,
            author=self.author
        )
        
        self.book2 = Book.objects.create(
            title="Book 2",
            publication_year=2021,
            author=self.author
        )
        
        self.client = APIClient()
    
    def test_list_authors(self):
        """
        Test GET /api/authors/
        Should return list of authors with nested books.
        Tests nested serializer functionality.
        """
        response = self.client.get('/api/authors/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Author')
        # Check nested books
        self.assertEqual(len(response.data[0]['books']), 2)
    
    def test_get_author_detail(self):
        """
        Test GET /api/authors/<id>/
        Should return author with all their books.
        """
        response = self.client.get(f'/api/authors/{self.author.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Author')
        self.assertEqual(len(response.data['books']), 2)
        
        # Verify book data structure
        first_book = response.data['books'][0]
        self.assertIn('title', first_book)
        self.assertIn('publication_year', first_book)
        self.assertIn('author', first_book)


class TestDatabaseIsolationTestCase(APITestCase):
    """
    Test to verify that test database is separate from production/development.
    This ensures data safety during testing.
    """
    
    def test_using_test_database(self):
        """
        Verify we're using a separate test database.
        Django creates and destroys this database for each test run.
        """
        from django.conf import settings
        
        # Test database is automatically configured
        # Data created here will not affect production
        
        author = Author.objects.create(name="Test Only Author")
        book = Book.objects.create(
            title="Test Only Book",
            publication_year=2023,
            author=author
        )
        
        # This data exists only during this test
        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(Book.objects.count(), 1)
        
        # After test completes, this data is destroyed
        # Production database remains untouched