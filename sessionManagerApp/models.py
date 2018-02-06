from django.db import models
from professorsApp.models import Professor
from coursesApp.models import Course
from django.contrib.auth.models import User
from datetime import timedelta, datetime, date

class Session(models.Model):
	DAYS_OF_WEEK_CHOICES = (
		('1', 'Saturday'),
		('2', 'Sunday'),
		('3', 'Monday'),
		('4', 'Tuesday'),
		('5', 'Wednesday'),
		('6', 'Thursday'),
		('7', 'Friday'),
	)
	professor = models.ForeignKey(Professor, null=True, blank=True, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	startTime = models.TimeField()
	endTime = models.TimeField(editable=False)
	dayOfWeek = models.CharField(max_length=1, choices=DAYS_OF_WEEK_CHOICES, default='1')
	location = models.CharField(max_length=15, default='P512')
	chatActive = models.BooleanField(default=False, blank=False, null=False)

	def save(self, *args, **kwargs):
		self.endTime = (datetime.combine(date(1, 1, 1), self.startTime) + timedelta(hours = self.course.duration.hour, minutes=self.course.duration.minute)).time()
		super(Session, self).save(*args, **kwargs)
		
	def __str__(self):
		if self.professor:
			return self.professor.name + " - " + self.course.name + " - " + str(self.get_dayOfWeek_display()) + " - "  + str(self.startTime) + " -> " + str(self.endTime)
		return "undefined" + " - " + self.course.name + " - " + str(self.get_dayOfWeek_display()) + " - "  + str(self.startTime) + " -> " + str(self.endTime)


class ChatFullName(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
	name = models.CharField(max_length=20, blank=False, null=False)
	session = models.ForeignKey(Session, on_delete=models.CASCADE)

	def __str__(self):
		return self.name