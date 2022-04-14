from math import log as logarithm

from django.conf import settings
from django.test import TestCase

from .mommy_recipes import airplane_recipe


class AirplaneModelTestCase(TestCase):

    def setUp(self):
        self.airplane_consumption = settings.AIRPLANE_FUEL_CONSUMPTION_PER_MINUTE_COEFFICIENT
        self.passanger_consumption = settings.PASSENGER_FUEL_CONSUMPTION_PER_MINUTE
        self.airplane_capacity = settings.AIRPLANE_FUEL_TANK_CAPACITY_COEFFICIENT

        self.airplane_1 = airplane_recipe.make(airplane_id=1, number_of_passenger=100)
        self.airplane_2 = airplane_recipe.make(airplane_id=2, number_of_passenger=200)
        self.airplane_3 = airplane_recipe.make(airplane_id=0, number_of_passenger=200)

    def test_fuel_consumption_per_minute_correct(self):
        fuel_consumption_per_minute_1 = (
            logarithm(1) * self.airplane_consumption + self.passanger_consumption * 100
        )
        fuel_consumption_per_minute_2 = (
            logarithm(2) * self.airplane_consumption + self.passanger_consumption * 200
        )
        fuel_consumption_per_minute_3 = self.passanger_consumption * 200

        self.assertEqual(self.airplane_1.fuel_consumption_per_minute, fuel_consumption_per_minute_1)
        self.assertEqual(self.airplane_2.fuel_consumption_per_minute, fuel_consumption_per_minute_2)
        self.assertEqual(self.airplane_3.fuel_consumption_per_minute, fuel_consumption_per_minute_3)

    def test_flight_maximum_minutes(self):
        flight_maximum_minutes_1 = (
            1 * self.airplane_capacity /
            (logarithm(1) * self.airplane_consumption + self.passanger_consumption * 100)
        )
        flight_maximum_minutes_2 = (
            2 * self.airplane_capacity /
            (logarithm(2) * self.airplane_consumption + self.passanger_consumption * 200)
        )
        flight_maximum_minutes_3 = 0

        self.assertEqual(self.airplane_1.flight_maximum_minutes, flight_maximum_minutes_1)
        self.assertEqual(self.airplane_2.flight_maximum_minutes, flight_maximum_minutes_2)
        self.assertEqual(self.airplane_3.flight_maximum_minutes, flight_maximum_minutes_3)
