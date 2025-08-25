from rest_framework import viewsets, permissions
from .models import Car, Driver
from .serializers import CarSerializer, DriverSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by("id")
    serializer_class = CarSerializer
    permission_classes = [permissions.AllowAny]


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all().order_by("id")
    serializer_class = DriverSerializer
    permission_classes = [permissions.AllowAny]
