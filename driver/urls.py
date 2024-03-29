from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet

router = DefaultRouter()
router.register(r'none', CarViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
