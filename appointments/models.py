from django.db import models
from business.models import * 
# Create your models here.

class TimeSlot(models.Model):
    business=models.ForeignKey(Business,on_delete=models.CASCADE)
    date=models.DateFieldField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    is_available=models.BooleanField(default=True)
    def __str__(self):
        return f"{self.date(self.start_time)}"

class Appointments(models.Model):
    STATUS_CHOICES=(
        ('pending','pending'),
        ('confirmed','confirmed'),
        ('canceled','canceled'),
    )
    business=models.ForeignKey(Business,on_delete=models.CASCADE)
    services=models.ForeignKey(Services,on_delete=models.CASCADE)
    customer_name=models.CharField(max_length=150)
    customer_phone=models.CharField(max_length=11)
    start_time=models.TimeField()
    end_time=models.TimeField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    created_at=models.TimeField(auto_now_add=True)
    def __str__(self):
        return f"self.customer_name-(self.services.name)"
