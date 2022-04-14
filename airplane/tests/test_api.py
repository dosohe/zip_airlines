from django.conf import settings
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from airplane.models import Airplane


class AirplaneAPITestCase(APITestCase):

    def setUp(self):
        self.request_data = [
            {
                "airplane_id": 1,
                "number_of_passenger": 100
            },
            {
                "airplane_id": 2,
                "number_of_passenger": 500
            },
            {
                "airplane_id": 4,
                "number_of_passenger": 400
            },
        ]
        self.invalid_request_format = {
            "airplane_id": 1,
            "number_of_passenger": 100
        }
        self.invalid_request_data = list(
            {'airplane_id': id, 'number_of_passenger': 100} for id in range(1, 12)
        )

    def _subject(self, data={}):
        url = reverse('airplanes-list')
        return self.client.post(url, data, format='json')

    def test_create_airplanes_success(self):
        response = self._subject(data=self.request_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Airplane.objects.count(), len(self.request_data))

    def test_create_single_airplane_success(self):
        single_airplane_date = {
            "airplane_id": 1,
            "number_of_passenger": 100,
        }
        response = self._subject(data=[single_airplane_date])
        single_airplane = Airplane.objects.first()
        expected_data = [{
            **single_airplane_date,
            "fuel_consumption_per_minute": single_airplane.fuel_consumption_per_minute,
            "flight_maximum_minutes": single_airplane.flight_maximum_minutes,
        }]

        self.assertEqual(Airplane.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), expected_data)

    def test_create_airplane_more_than_allowed(self):
        """
        Posting more planes than set by MAX_AIRPLANES_NUMBER is not allowed
        """
        response = self._subject(data=self.invalid_request_data)
        expected_error = {
            'error': f'ValueError: Number of {settings.MAX_AIRPLANES_NUMBER} planes is allowed'
        }

        self.assertEqual(Airplane.objects.count(), 0)
        self.assertEqual(response.status_code, 422)
        self.assertDictEqual(response.data, expected_error)

    def test_create_airplane_with_invalid_format(self):
        """
        Posting the planes with a wrong format
        """
        response = self._subject(data=self.invalid_request_format)

        expected_error = {'error': 'TypeError: Wrong format, use a list'}
        self.assertEqual(Airplane.objects.count(), 0)
        self.assertEqual(response.status_code, 422)
        self.assertDictEqual(response.data, expected_error)
