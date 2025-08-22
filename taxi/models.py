from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class Driver(AbstractUser):
    pass


class Car(models.Model):
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20, unique=True)
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars",
        blank=True
    )

    def __str__(self):
        return f"{self.manufacturer} {self.model} ({self.license_plate})"
