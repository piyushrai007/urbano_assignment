
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class EmailVerificationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='Str0ngP@ssw0rd!', email='testuser@example.com')
        self.user.is_active = False
        self.user.save()
        self.uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        self.token = self.user.password  # Using password hash as a token example (not recommended in production)

    def test_email_verification(self):
        url = reverse('activate', args=[self.uid, self.token])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Account activated successfully', response.data['message'])