from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text

class Answer(models.Model):
    text = models.CharField(max_length=250)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class OnlineExam(models.Model):
    date_time_start = models.DateTimeField()
    duration = models.IntegerField()
    quiz_grade = models.IntegerField()

    def __str__(self):
        return ""