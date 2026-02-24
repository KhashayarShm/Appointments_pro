from django.db import models
from django.contrib.auth.models import User

class Business(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=11)
    address = models.TextField(blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Services(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    duration = models.PositiveIntegerField(help_text="time in minutes")
    price = models.PositiveIntegerField()
    active = models.BooleanField(default=False)   

    def __str__(self):
        return f"{self.name} ({self.business.name})"   

