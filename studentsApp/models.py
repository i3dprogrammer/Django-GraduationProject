from django.contrib.auth.models import User
from django.db import models

from departmentsApp.models import Group
from sessionManagerApp.models import Session


# Why the fuck StudentInfo not Student? xD
class StudentInfo(models.Model):
	user = models.OneToOneField(User)
	year = models.IntegerField(default=1)
	group = models.ForeignKey(Group, default=23)
	sessions = models.ManyToManyField(Session, blank=True)
	full_name = models.CharField(max_length=100, default='Ahmed Magdy Mohammed Essa')

	def __str__(self):
		return self.user.username + " - " + str(self.sessions.count()) + " Sessions."

