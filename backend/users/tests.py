from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User


class UserAuthTests(APITestCase):
    def test_registration_and_login(self):
        url = reverse('register')
        data = {
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'strongpass123',
            'role': User.Role.JOBSEEKER,
        }
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, 201)

        # Login
        url = reverse('token_obtain_pair')
        resp = self.client.post(url, {'username': 'alice', 'password': 'strongpass123'}, format='json')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('access', resp.data)
        self.assertIn('refresh', resp.data)
