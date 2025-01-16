from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Category, Book
from rest_framework.reverse import reverse


class BookAPITestCase(APITestCase):

    def setUp(self):
        # User yaratish
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Category yaratish
        self.category = Category.objects.create(name='Fiction')

        # Book yaratish
        self.book = Book.objects.create(
            title='Sample Book',
            author=self.user,
            category=self.category,
            published_date='2025-01-16',
            isbn='1234567890123'
        )

    def test_create_book(self):
        """
        Test Book yaratish (POST)
        """
        url = reverse('bookviewset-list')
        data = {
            'title': 'New Book',
            'author': self.user.id,
            'category': self.category.id,
            'published_date': '2025-02-10',
            'isbn': '9876543210987'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(title='New Book').isbn, '9876543210987')

        print("Test 'test_create_book' muvaffaqiyatli yakunlandi ✅ \n")

    def test_list_books(self):
        """
        Test Booklar ro'yxatini olish (GET)
        """
        url = reverse('bookviewset-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        print("Test 'test_list_books' muvaffaqiyatli yakunlandi ✅ \n")

    def test_get_book(self):
        """
        Test bitta Kitobni olish (GET)
        """
        url = reverse('bookviewset-detail', kwargs={'pk': self.book.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)
        self.assertEqual(response.data['isbn'], self.book.isbn)

        print("Test 'test_get_book' muvaffaqiyatli yakunlandi ✅ \n")

    def test_delete_book(self):
        """
        Test Kitobni o‘chirish (DELETE)
        """
        url = reverse('bookviewset-detail', kwargs={'pk': self.book.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

        print("Test 'test_delete_book' muvaffaqiyatli yakunlandi ✅ \n")

    def test_create_category(self):
        """
        Test Category yaratish (POST)
        """
        url = reverse('category-list')
        data = {'name': 'Science Fiction'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)
        self.assertEqual(Category.objects.get(name='Science Fiction').name, 'Science Fiction')

        print("Test 'test_create_category' muvaffaqiyatli yakunlandi ✅ \n")

    def test_list_category(self):
        """
        Test Categories ro'yxatini olish (GET)
        """
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        print("Test 'test_list_category' muvaffaqiyatli yakunlandi ✅ \n")

    def test_get_category(self):
        """
        Test bitta Category olish (GET)
        """
        url = reverse('category-detail', kwargs={'pk': self.category.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.category.name)

        print("Test 'test_get_category' muvaffaqiyatli yakunlandi ✅ \n")
