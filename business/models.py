from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Business(models.Model):
	owner=models.Foreignkey(User,on_delete=models.CASCADE)
	name=models.CharField(max_length=150)
	phone=models.CharField(max_length=11)
	address=models.TextField(blank=True)
	description=models.TextField(blank=True)
	created=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
	



class Services(models.Model):

    business=models.ForeignKey(Business,on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    duration=models.PositiveIntegerField(help_text="time in minutes range")
    price=models.PositiveIntegerField()
    activate=models.BooleanField(default=False)
    def __str_(self):
      return f"{self.name(self.business.name)}"
