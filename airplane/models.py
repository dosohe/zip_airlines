from math import log as logarithm

from django.conf import settings
from django.db import models

from django_extensions.db.models import TimeStampedModel


class Airplane(TimeStampedModel):

    airplane_id = models.PositiveIntegerField()
    number_of_passenger = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'number {self.airplane_id} with {self.number_of_passenger} passengers'

    @property
    def fuel_consumption_per_minute(self) -> float:
        fuel_consumption_per_minute = (
            logarithm(self.airplane_id) * settings.AIRPLANE_FUEL_CONSUMPTION_PER_MINUTE_COEFFICIENT
            if self.airplane_id != 0
            else 0
        )
        return (
            fuel_consumption_per_minute + settings.PASSENGER_FUEL_CONSUMPTION_PER_MINUTE
            * self.number_of_passenger
        )

    @property
    def flight_maximum_minutes(self) -> float:
        capacity = self.airplane_id * settings.AIRPLANE_FUEL_TANK_CAPACITY_COEFFICIENT
        return (
            capacity / self.fuel_consumption_per_minute
            if self.fuel_consumption_per_minute != 0
            else 0
        )
