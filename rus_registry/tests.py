from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class RusRegistryServerViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.data = {
            'cad_number': '123456',
            'latitude': 55.7558,
            'longitude': 37.6173
        }
        self.url = reverse('rus_registry:rus_registry')

    def test_valid_request(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_request(self):
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'error': 'Invalid request data'})

    def test_missing_cad_number(self):
        response = self.client.post(self.url,)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'error': 'Invalid request data'})
