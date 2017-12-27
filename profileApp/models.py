from django.db import models
from studentsApp.models import StudentInfo
from coursesApp.models import Course
# Create your models here.

class PublicNotification(models.Model):
	showToStudents = models.BooleanField(default=True)
	showToProfessors = models.BooleanField(default=False)
	notification = models.CharField(max_length=100)

	def __str__(self):
		return self.notification[:100]

class UserSemester(models.Model):
	info = models.ForeignKey(StudentInfo)
	GPA = models.FloatField(default=0.0)

	def updateGPA(self): # TODO: Fix this, this is temporary.
		gpa = 0.0
		for c_c in self.completedcourse_set.all():
			gpa += ((c_c.written_result + c_c.oral_result + c_c.app_result) / 
				(c_c.course.max_written_result + c_c.course.max_oral_result + c_c.course.max_app_result) / 2)
		self.GPA = gpa
		self.save()

	def __str__(self):
		return str(self.id) + "# " + self.info.user.first_name + " " + self.info.user.last_name

class CompletedCourse(models.Model):
	semester = models.ForeignKey(UserSemester)
	course = models.ForeignKey(Course)
	written_result = models.IntegerField()
	oral_result = models.IntegerField()
	app_result = models.IntegerField()
	# 
	def save(self, *args, **kwargs):
		self.semester.updateGPA()
		super(CompletedCourse, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.course)