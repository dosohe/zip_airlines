from rest_framework import serializers

from .models import Airplane


class AirplaneSerializer(serializers.ModelSerializer):
    fuel_consumption_per_minute = serializers.SerializerMethodField(
        source='get_fuel_consumption_per_minute'
    )
    flight_maximum_minutes = serializers.SerializerMethodField(
        source='get_flight_maximum_minutes'
    )

    class Meta:
        model = Airplane
        fields = (
            'airplane_id',
            'number_of_passenger',
            'fuel_consumption_per_minute',
            'flight_maximum_minutes',
        )

    @staticmethod
    def get_fuel_consumption_per_minute(obj) -> float:
        return obj.fuel_consumption_per_minute

    @staticmethod
    def get_flight_maximum_minutes(obj) -> float:
        return obj.flight_maximum_minutes
