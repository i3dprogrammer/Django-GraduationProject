from django.db import models
from sessionManagerApp.models import Session

class OnlineExam(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    date_time_start = models.DateTimeField()
    duration = models.IntegerField()
    quiz_grade = models.IntegerField()

    def __str__(self):
        return self.session.course.name

class Question(models.Model):
    text = models.CharField(max_length=250)
    exam = models.ForeignKey(OnlineExam, on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class Answer(models.Model):
    text = models.CharField(max_length=250)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.text