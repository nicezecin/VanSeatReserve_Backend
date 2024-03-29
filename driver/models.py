from django.db import models


# Create your models here.
class Car(models.Model):
    no = models.CharField(max_length=3, unique=True, default="")
    carNumber = models.CharField(max_length=10, unique=True)
