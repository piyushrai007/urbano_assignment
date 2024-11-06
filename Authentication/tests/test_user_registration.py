
from django.core import mail
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class UserRegistrationTestCase(TestCase):
    def test_register_user(self):
        url = reverse('signup')
        data = {
            "username": "piyush",
            "password": "Str0ngP@ssw0rd!",
            "email": "piyushraivds45@gmail.com"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(mail.outbox), 1)  # Check that one email was sent
        email = mail.outbox[0]
        self.assertEqual(email.subject, 'Activate your account')
        self.assertIn('Check your email to activate your account.', response.data['message'])