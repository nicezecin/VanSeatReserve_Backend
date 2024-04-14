from django.db import models
from user.models import User
from route.models import AddRoutes
from car.models import Seat


# import random
# import string

STATUS = [
    ("unpaid", "ยังไม่ชำระเงิน"),
    ("pending", "รอการตรวจสอบ"),
    ("paid", "ชำระเงินสำเร็จ"),
    ("checked", "ตรวจสอบสถานะการชำระเงินแล้ว")
]

STATUSAPPROVE = [
    ("reject", "ไม่อนุมัติ"),
    ("approve", "อนุมติ"),
    ("pending", "รอดำเนินกาาร"),
]


# Create your models here.
class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    add_route = models.ForeignKey(
        AddRoutes, on_delete=models.CASCADE, null=True, blank=True
    )
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, null=True, blank=True)
    img = models.ImageField(upload_to="tickets/", null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default="unpaid")
    payDate = models.DateField(null=True, blank=True)
    payTime = models.TimeField(null=True, blank=True)
    payPrice = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
        )
    statusApprove = models.CharField(max_length=20, choices=STATUSAPPROVE, default="pending")

    
