from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, DriverViewSet

router = DefaultRouter()
router.register(r"cars", CarViewSet, basename="car")
router.register(r"drivers", DriverViewSet, basename="driver")

urlpatterns = [
    path("", include(router.urls)),
]
