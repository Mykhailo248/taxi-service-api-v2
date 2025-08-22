from django.contrib import admin
from .models import Driver, Car

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "is_active", "is_staff", "date_joined")
    search_fields = ("username", "email")

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "manufacturer", "model", "license_plate")
    search_fields = ("manufacturer", "model", "license_plate")
    filter_horizontal = ("drivers",)
