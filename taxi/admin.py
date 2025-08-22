from django.contrib import admin
from .models import Driver

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "is_active", "is_staff", "date_joined")
    search_fields = ("username", "email")
