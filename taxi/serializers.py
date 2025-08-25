from rest_framework import serializers
from .models import Car, Driver
from .tasks import send_welcome_email

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["id", "manufacturer", "model", "license_plate", "drivers"]
        read_only_fields = ["id"]


class DriverSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Driver
        fields = ["id", "username", "email", "password"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        driver = Driver(**validated_data)
        driver.set_password(password)
        driver.save()
        # Виклик Celery таски
        send_welcome_email.delay(driver.email, driver.username)
        return driver