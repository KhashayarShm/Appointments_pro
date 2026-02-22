from django.db import models
from appointments.models import *
# Create your models here.
class Payments(models.Model):
    appointment=models.ForeignKey(Appointments,on_delete=models.CASCADE)
    amount=models.PositiveIntegerField()
    status=models.CharField(max_length=20,default='pending')
    transaction_id=models.CharField(max_length=200,blank=True)
    created_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return f"payment{self.amount}for{self.appointment.id}"
