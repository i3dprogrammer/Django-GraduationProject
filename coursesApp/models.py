from django.db import models
from departmentsApp.models import Group

class Course(models.Model):
	code = models.CharField(max_length=15, default='#A312', unique=True)
	name = models.CharField(max_length=100)
	elective = models.BooleanField(default=False)
	duration = models.TimeField(default='02:00:00')
	applications_duration = models.TimeField(default='02:00:00')
	max_written_result = models.IntegerField(default=140)
	max_oral_result = models.IntegerField(default=20)
	max_app_result = models.IntegerField(default=40)
	info = models.TextField(max_length=1000, null=True, blank=True)
	group = models.ForeignKey(Group, default=1, on_delete=models.CASCADE)
	prequels = models.ManyToManyField("Course", blank=True, related_name="prerequisites+")
	
	def __str__(self):
		return "#" + self.code + " - " + self.name