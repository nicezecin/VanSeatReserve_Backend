from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, SeatViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'seats', SeatViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
