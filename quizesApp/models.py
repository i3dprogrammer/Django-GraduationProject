from django.db import models
from studentsApp.models import StudentInfo
from sessionManagerApp.models import Session


class QuizComplete(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    answerFile = models.FileField(upload_to='answers/%Y/%m/%d/%H/%M/')
    grade = models.CharField(max_length=10, default="---")

    def __str__(self):
        return str(self.student.id) + " " + self.student.full_name

class Quiz(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    quizFile = models.FileField(upload_to='quizes/%Y/%m/%d/%H/%M/')
    studentsCompleted = models.ManyToManyField(QuizComplete, blank=True)
    deadline = models.DateTimeField()
    max_grade = models.IntegerField(default=10)

    def __str__(self):
        return str(self.id) + " - " + str(self.session)