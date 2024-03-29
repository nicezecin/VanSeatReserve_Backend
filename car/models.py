from django.db import models
from user.models import User

# Create your models here.
class Car(models.Model):
    driver = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    no = models.CharField(max_length=3, unique=True, default="")
    carNumber = models.CharField(max_length=10, unique=True)
