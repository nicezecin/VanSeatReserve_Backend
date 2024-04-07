from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet, TicketView


router = DefaultRouter()
router.register(r'tickets', TicketViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('tickets_filter/', TicketView.as_view(), name='tickets_filter'),
    
    
]
