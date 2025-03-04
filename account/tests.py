from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import CustomUser


class LoginUserTest(APITestCase):
    def setUp(self):
        # Create a user for testing
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@gmail.com',
            'password': 'testPassword123'
        }
        self.user = CustomUser.objects.create_user(**self.user_data)

    def test_login_with_valid_credential_username(self):
        # Test login with valid username
        login_data = {
            'username_or_email': self.user_data['username'],
            'password': self.user_data['password']
        }
        response = self.client.post(reverse('login'), data=login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
  
    def test_login_with_valid_credential_email(self):
        # Test login with valid email
        login_data = {
            'username_or_email': self.user_data['email'],
            'password': self.user_data['password']
        }
        response = self.client.post(reverse('login'), data=login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_login_with_invalid_username(self):
        # Test login with invalid username
        login_data = {
            'username_or_email': 'wronguser',
            'password': self.user_data['password']
        }
        response = self.client.post(reverse('login'), data=login_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)

    def test_login_with_invalid_email(self):
        # Test login with invalid username
        login_data = {
            'username_or_email': 'wronguser@gmail.com',
            'password': self.user_data['password']
        }
        response = self.client.post(reverse('login'), data=login_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)

    def test_login_with_invalid_password(self):
        # Test login with invalid password
        login_data = {
            'username': self.user_data['username'],
            'password': 'wrongPassword@'
        }
        response = self.client.post(reverse('login'), data=login_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)
