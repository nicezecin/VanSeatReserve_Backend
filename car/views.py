from rest_framework import viewsets
from .models import Car, Seat
from .serializer import CarSerializer, SeatSerializer
from rest_framework.response import Response
from rest_framework import status

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        queryset = Seat.objects.all()
        car_id = self.request.query_params.get("car_id")
        no = self.request.query_params.get("no")
        status = self.request.query_params.get("status")
        
        if car_id:
            queryset = queryset.filter(car_id=car_id)        
        if no:
            queryset = queryset.filter(no__exact=no)
        if status:
            queryset = queryset.filter(status__icontains=status)
            
            
        return queryset
    
    # Method to update seat status by ID using PUT request
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
