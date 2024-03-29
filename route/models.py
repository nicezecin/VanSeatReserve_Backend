from django.db import models
from car.models import Car

# Create your models here.
class Routes(models.Model):
    name = models.CharField(max_length=255, unique=True)

class AddRoutes(models.Model):
    startRoute = models.ForeignKey(
        Routes, on_delete=models.CASCADE, null=True, blank=True, related_name='start_routes')
    endRoute = models.ForeignKey(
        Routes, on_delete=models.CASCADE, null=True, blank=True, related_name='end_routes')
    date = models.DateField()
    time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE, null=True, blank=True)
    
