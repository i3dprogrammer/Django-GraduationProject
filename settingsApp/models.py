from django.db import models

class Setting(models.Model):
	canChangeSessions = models.BooleanField(default=False)
	minHoursWeek = models.IntegerField(default=10)
	maxHoursWeek = models.IntegerField(default=10)
	maxStudentYear = models.IntegerField(default=4)
	
    #Should disallow deleting or adding more than 1 row, we only require 1 ROW.
    
	def __str__(self):
		return 'Select settings'