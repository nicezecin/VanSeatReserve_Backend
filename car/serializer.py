from rest_framework import serializers
from .models import Car, Seat
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
class SeatSerializer(serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(
        queryset=Car.objects.all(),
        required=False
        
    )
    
    car_id = CarSerializer(source='car', read_only=True)
    
    
    class Meta:
        model = Seat
        fields = '__all__'
        dept = 2
         
        
        
