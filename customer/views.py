from rest_framework import viewsets
from .models import Ticket
from .serializer import TicketSerializer
from rest_framework.response import Response
from rest_framework import status

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
