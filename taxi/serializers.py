from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["id", "manufacturer", "model", "license_plate", "drivers"]
        read_only_fields = ["id"]
