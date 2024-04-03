from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet

from .views import upload_file

router = DefaultRouter()
router.register(r'tickets', TicketViewSet)
urlpatterns = [
    path('', include(router.urls)),
    
    # upload file 
    path('api/upload/', upload_file, name='upload_file'),
]
