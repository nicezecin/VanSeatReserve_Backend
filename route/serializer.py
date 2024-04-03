from rest_framework import serializers
from .models import  Routes, AddRoutes
from car.models import Car
from car.serializer import CarSerializer
from user.serializer import UserSerializer
from user.models import User

class RoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = '__all__'
        dept = 2
         
class AddRoutesSerializer(serializers.ModelSerializer):
    driver = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=True 
    )
    startRoute = serializers.PrimaryKeyRelatedField(
        queryset=Routes.objects.all(),
        required=True 
    )
    endRoute = serializers.PrimaryKeyRelatedField(
        queryset=Routes.objects.all(),
        required=True      
    )
    car = serializers.PrimaryKeyRelatedField(
        queryset=Car.objects.all(),
        required=True      
    )
    driver_id = UserSerializer(source='driver', read_only=True)
    startRoute_id = RoutesSerializer(source='startRoute', read_only=True)
    endRoute_id = RoutesSerializer(source='endRoute', read_only=True)
    car_id = CarSerializer(source='car', read_only=True)
    
    class Meta:
        model = AddRoutes
        fields = '__all__'
        dept = 2
        
        
