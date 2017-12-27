from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(null=True, blank=True)
	info = models.CharField(max_length=5000)
	location = models.CharField(max_length=100)
	date = models.DateTimeField()
	usersGoing = models.ManyToManyField(User, related_name='users_attending', blank=True)
	usersInterested = models.ManyToManyField(User, related_name='users_thinking', blank=True)
	
	def __str__(self):
		return self.name