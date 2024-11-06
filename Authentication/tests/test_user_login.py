# FILE: Authentication/tests/test_user_login.py

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class UserLoginTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='Str0ngP@ssw0rd!', email='testuser@example.com')
        self.user.is_active = True
        self.user.save()

    def test_login_user(self):
        url = reverse('login')
        data = {
            "username": "testuser",
            "password": "Str0ngP@ssw0rd!"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)