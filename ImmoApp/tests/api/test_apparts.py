import pytest
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

client = APIClient()


class TestList(APITestCase):
    def test_list(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_appartement(self):
        response = self.client.get(reverse('saison'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
