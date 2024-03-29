from rest_framework import serializers
from .models import Car
from user.models import User
from user.serializer import UserSerializer

class CarSerializer(serializers.ModelSerializer):

    
    
    class Meta:
        model = Car
        fields = '__all__'
        dept = 2
         
        
        
