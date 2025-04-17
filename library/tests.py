from django.test import TestCase

# Create your tests here.


from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from .models import Book

class BookAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = get_user_model().objects.create_user(email="shubhamjadhav.code@gmail.com", password="12345")
        self.client.force_authenticate(user=self.admin)

    def test_create_book(self):
        data = {
            "title": "Test Book",
            "author": "Shubham's Test",
            "isbn": "1234567890123",
            "publication_date": "2025-18-04"
        }
        response = self.client.post("/api/books/", data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 1)

    def test_student_book_list(self):
        Book.objects.create(title="RISE OF AI", author="Shubham Jadhab", isbn="1234567890123", publication_date="2025-18-04")
        response = self.client.get("/student/books/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)
