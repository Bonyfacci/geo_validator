from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Address, Request
from .serializers import RequestSerializer
import json


class AddressAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('app_geo:address')
        self.valid_data = {
            'cad_number': '123456',
            'latitude': 55.7558,
            'longitude': 37.6173
        }
        self.invalid_data = {
                'cad_number': '',
                'latitude': 'invalid',
                'longitude': 'invalid'
            }

    def test_create_address(self):
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Address.objects.count(), 1)
        self.assertEqual(Request.objects.count(), 1)

    def test_create_address_invalid_data(self):

        response = self.client.post(self.url, self.invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Address.objects.count(), 0)
        self.assertEqual(Request.objects.count(), 0)


class RequestAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.address = Address.objects.create(
            cad_number='123456',
            latitude=55.7558,
            longitude=37.6173
        )
        self.request = Request.objects.create(
            address=self.address,
            response='true'
        )
        self.url = reverse('app_geo:result_request', kwargs={'pk': self.request.pk})
        self.fake_url = reverse('app_geo:result_request', kwargs={'pk': 999})

    def test_retrieve_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), RequestSerializer(self.request).data)

    def test_retrieve_request_not_found(self):
        response = self.client.get(self.fake_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class HistoryAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.address1 = Address.objects.create(
            cad_number='123456',
            latitude=55.7558,
            longitude=37.6173
        )
        self.address2 = Address.objects.create(
            cad_number='789012',
            latitude=55.7558,
            longitude=37.6173
        )
        self.request1 = Request.objects.create(
            address=self.address1,
            response='true'
        )
        self.request2 = Request.objects.create(
            address=self.address2,
            response='false'
        )
        self.url = reverse('app_geo:history_requests')

    def test_list_requests(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), RequestSerializer(Request.objects.all(), many=True).data)

    def test_search_requests(self):
        response = self.client.get(f"{self.url}?search=123456")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),
                         RequestSerializer(Request.objects.filter(address__cad_number='123456'), many=True).data)


class PingAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('app_geo:ping_check')

    def test_ping(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '"Сервер запущен"')
