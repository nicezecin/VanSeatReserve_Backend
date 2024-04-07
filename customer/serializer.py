from rest_framework import serializers
from .models import Ticket
from user.models import User
from user.serializer import UserSerializer
from route.models import AddRoutes
from route.serializer import AddRoutesSerializer
from car.models import Car
from car.serializer import CarSerializer
from car.models import Seat
from car.serializer import SeatSerializer

class TicketSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False 
    )
    
    add_route = serializers.PrimaryKeyRelatedField(
        queryset=AddRoutes.objects.all(),
        required=False 
    )
    
    seat = serializers.PrimaryKeyRelatedField(
        queryset=Seat.objects.all(),
        required=False 
    )
    
    
    user_id = UserSerializer(source='user', read_only=True)
    add_route_id = AddRoutesSerializer(source='add_route', read_only=True)
    seat_id = SeatSerializer(source='seat', read_only=True) 

    
    
    class Meta:
        model = Ticket
        fields = '__all__'
        dept = 2
        
    
        
        
