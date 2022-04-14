from django.conf.urls import include
from django.urls import path

from rest_framework.routers import DefaultRouter

from airplane import api

router = DefaultRouter()
router.register('airplanes', api.AirplaneViewSet, basename='airplanes')

urlpatterns = [
    path('api/', include(router.urls)),
]
