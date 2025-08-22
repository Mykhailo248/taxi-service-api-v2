from rest_framework import viewsets, permissions
from .models import Car
from .serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by("id")
    serializer_class = CarSerializer
    permission_classes = [permissions.AllowAny]
