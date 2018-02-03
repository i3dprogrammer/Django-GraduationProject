from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Professor(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	info = models.TextField(max_length=1000)
	image = models.ImageField(null=True, blank=True)
	hidden = models.BooleanField(default=False)
	
	def __str__(self):
		return self.name
	
