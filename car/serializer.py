from rest_framework import serializers
from .models import Car
from user.models import User
from user.serializer import UserSerializer

class CarSerializer(serializers.ModelSerializer):
    driver = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=True 
        
    )
    
    driver_id = UserSerializer(source='driver', read_only=True)
    
    
    class Meta:
        model = Car
        fields = '__all__'
        dept = 2
         
        
        
