# Book API - Authentication Guide

## Overview
This API uses Token Authentication to secure endpoints.

## Authentication

### Obtaining a Token
Send POST request to `/api/auth/token/` with username and password:
```bash
POST /api/auth/token/
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
```

Response:
```json
{
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### Using the Token
Include the token in the Authorization header:

## Permissions

### Read Operations (GET)
- Anyone can read books (no authentication required)

### Write Operations (POST, PUT, PATCH, DELETE)
- Requires valid authentication token

## Endpoints

| Endpoint | Method | Auth Required | Description |
|----------|--------|---------------|-------------|
| `/api/auth/token/` | POST | No | Get authentication token |
| `/api/books/` | GET | No | List all books (simple) |
| `/api/books_all/` | GET | No | List all books |
| `/api/books_all/` | POST | Yes | Create new book |
| `/api/books_all/{id}/` | GET | No | Get single book |
| `/api/books_all/{id}/` | PUT | Yes | Update book |
| `/api/books_all/{id}/` | PATCH | Yes | Partial update |
| `/api/books_all/{id}/` | DELETE | Yes | Delete book |

## Example Requests

### Get Token
```bash
curl -X POST http://localhost:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"your_password"}'
```

### List Books (No Auth)
```bash
curl http://localhost:8000/api/books_all/
```

### Create Book (With Auth)
```bash
curl -X POST http://localhost:8000/api/books_all/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -d '{
    "title": "New Book",
    "author": "Author Name",
    "publication_year": 2024
  }'
```

### Update Book (With Auth)
```bash
curl -X PUT http://localhost:8000/api/books_all/1/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -d '{
    "title": "Updated Title",
    "author": "Updated Author",
    "publication_year": 2024
  }'
```

### Delete Book (With Auth)
```bash
curl -X DELETE http://localhost:8000/api/books_all/1/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```