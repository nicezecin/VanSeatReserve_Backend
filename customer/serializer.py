from rest_framework import serializers
from .models import Ticket
from user.models import User
from user.serializer import UserSerializer
from route.models import AddRoutes
from route.serializer import AddRoutesSerializer

class TicketSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=True 
    )
    
    add_route = serializers.PrimaryKeyRelatedField(
        queryset=AddRoutes.objects.all(),
        required=True 
    )
    
    user_id = UserSerializer(source='user', read_only=True)
    add_route_id = AddRoutesSerializer(source='add_route', read_only=True)
    
    
    class Meta:
        model = Ticket
        fields = '__all__'
        dept = 2
        
    
        
        
