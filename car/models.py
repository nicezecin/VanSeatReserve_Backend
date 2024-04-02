from django.db import models
#from user.models import User


# Create your models here.
STATUS = [("unavailable", "ไม่ว่าง"), ("available", "ว่าง")]
class Car(models.Model):
    no = models.CharField(max_length=3, unique=True, default="")
    carNumber = models.CharField(max_length=10, unique=True)

class Seat(models.Model):
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE, null=True, blank=True)
    no = models.CharField(max_length=3, default="")
    status = models.CharField(max_length=20, choices=STATUS, default="available")

   
    