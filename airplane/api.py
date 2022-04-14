from django.conf import settings

from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from .models import Airplane
from .serializers import AirplaneSerializer


class AirplaneViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = AirplaneSerializer
    queryset = Airplane.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            airplanes_data = request.data
            if not isinstance(airplanes_data, list):
                raise TypeError("Wrong format, use a list")
            if len(airplanes_data) > settings.MAX_AIRPLANES_NUMBER:
                raise ValueError(f'Number of {settings.MAX_AIRPLANES_NUMBER} planes is allowed')

            serializer = AirplaneSerializer(data=airplanes_data, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        except (TypeError, ValueError) as error:
            return Response({'error': f'{error.__class__.__name__}: {error}'}, status=422)
