from rest_framework import viewsets
from .models import Ticket
from .serializer import TicketSerializer
from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def get_queryset(self):
        queryset = Ticket.objects.all()
        user_id = self.request.query_params.get("user_id")
        add_route_id = self.request.query_params.get("add_route_id")
        seat_id = self.request.query_params.get("seat_id")
        img = self.request.query_params.get("img")
        status = self.request.query_params.get("status")
        
        if user_id:
            queryset = queryset.filter(user_id=user_id)        
        if add_route_id:
            queryset = queryset.filter(add_route_id=add_route_id)
        if seat_id:
            queryset = queryset.filter(seat_id=seat_id)
        if img:
            queryset = queryset.filter(img__icontains=img)
        if status:
            queryset = queryset.filter(status__icontains=status)
            
            
        return queryset
    
# upload file img    
@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        file_name = default_storage.save(uploaded_file.name, ContentFile(uploaded_file.read()))
        return JsonResponse({'message': 'File uploaded successfully'})
    return JsonResponse({'error': 'No file uploaded'}, status=400)
