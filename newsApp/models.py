from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class News(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	news_title = models.CharField(max_length=100)
	news_desc = models.CharField(max_length=5000)
	news_date = models.DateTimeField("Date published")
	
	def __str__(self):
		return self.news_title