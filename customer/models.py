from django.db import models
from user.models import User
from route.models import AddRoutes
from car.models import Car
from car.models import Seat
import uuid


STATUS = [("unpaid", "ยังไม่ชำระเงิน"), ("pending", "รอการตรวจสอบ"), ("paid", "ชำระเงินสำเร็จ")]
# Create your models here.
class Ticket(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    add_route = models.ForeignKey(
        AddRoutes, on_delete=models.CASCADE, null=True, blank=True)
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE, null=True, blank=True, related_name='tickets')
    seat = models.ForeignKey(
        Seat, on_delete=models.CASCADE, null=True, blank=True, related_name='tickets')
    img = models.ImageField(upload_to='tickets/', null=True, blank=True) 
    status = models.CharField(max_length=20, choices=STATUS, default="unpaid")
    ticket_no =  models.CharField(max_length=20, default="")  

    def __str__(self):
        return self.ticket_no
    
    def save(self, *args, **kwargs):
        if not self.ticket_no:
            # Generate ticket number using UUID
            self.ticket_no = str(uuid.uuid4()).replace("-", "")[:20]  
        super().save(*args, **kwargs)
