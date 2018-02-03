from django.db import models
from professorsApp.models import Professor
from coursesApp.models import Course
from django.contrib.auth.models import User
from datetime import timedelta, datetime, date
#from channels import Group

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

	# def chat_getCharGroup(self):
	# 	return 'chat-{0}'.format(self.id)

	# def chat_addUserToGroup(self, reply_channel):
	# 	Group(self.chat_getCharGroup()).add(reply_channel)

	# def chat_broadcastMessage(self, text, user, system = False):
	# 	broadcasted_message = ''
	# 	if System:
	# 		broadcasted_message = '[System] {0} {1}'.format(user, text)
	# 	else:
	# 		broadcasted_message = '[{0}] {1}'.format(user, text)

	# 	Group(self.chat_getCharGroup()).send({
	# 		'text': broadcasted_message,
	# 	})

	def save(self, *args, **kwargs):
		self.endTime = (datetime.combine(date(1, 1, 1), self.startTime) + timedelta(hours = self.course.duration.hour, minutes=self.course.duration.minute)).time()
		super(Session, self).save(*args, **kwargs)
		
	def __str__(self):
		if self.professor:
			return self.professor.name + " - " + self.course.name + " - " + str(self.get_dayOfWeek_display()) + " - "  + str(self.startTime) + " -> " + str(self.endTime)
		return "undefined" + " - " + self.course.name + " - " + str(self.get_dayOfWeek_display()) + " - "  + str(self.startTime) + " -> " + str(self.endTime)

''' class UserInfo(models.Model):
	user = models.OneToOneField(User)
	sessions = models.ManyToManyField(Session, blank=True)

	def __str__(self):
		return self.user.username + " - " + str(self.sessions.count()) + " Sessions."
		 '''