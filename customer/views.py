from rest_framework import viewsets
from .models import Ticket
from .serializer import TicketSerializer
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .filters import TicketFilter



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
        id = self.request.query_params.get("id")
        statusApprove = self.request.query_params.get("statusApprove")
        payDate = self.request.query_params.get("payDate")
        payTime = self.request.query_params.get("payTime")
        payPrice = self.request.query_params.get("payPrice")
        
        if user_id:
            queryset = queryset.filter(user_id=user_id)        
        if add_route_id:
            queryset = queryset.filter(add_route_id=add_route_id)
        if seat_id:
            queryset = queryset.filter(seat_id=seat_id)
        if img:
            queryset = queryset.filter(img__icontains=img)
        if status:
            queryset = queryset.filter(status__exact=status)
        if id:
            queryset = queryset.filter(id=id)
        if statusApprove:
            queryset = queryset.filter(statusApprove__exact=statusApprove)
        if payDate:
            queryset = queryset.filter(payDate__icontains=payDate)
        if payTime:
            queryset = queryset.filter(payTime__icontains=payTime)
        if payPrice:
            queryset = queryset.filter(payPrice__icontains=payPrice)
        
        
            
          
            
        return queryset
    
        # Method to update seat status by ID using PUT request
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    
class TicketView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TicketFilter
