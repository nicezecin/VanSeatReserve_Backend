from rest_framework import viewsets
from .models import Routes, AddRoutes
from .serializer import RoutesSerializer, AddRoutesSerializer
from rest_framework.response import Response
from rest_framework import status

class RoutesViewSet(viewsets.ModelViewSet):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get("name")
        
        if name:
            queryset = queryset.filter(name__icontains=name)
            
        return queryset

    
class AddRoutesViewSet(viewsets.ModelViewSet):
    queryset = AddRoutes.objects.all()
    serializer_class = AddRoutesSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def get_queryset(self):
        queryset = super().get_queryset()
        startRoute_id = self.request.query_params.get("startRoute_id")
        endRoute_id = self.request.query_params.get("endRoute_id")
        date = self.request.query_params.get("date")
        

        if startRoute_id:
            queryset = queryset.filter(startRoute_id=startRoute_id)
        if endRoute_id:
            queryset = queryset.filter(endRoute_id=endRoute_id)
        if date:
            queryset = queryset.filter(date__icontains=date)
            
        return queryset
