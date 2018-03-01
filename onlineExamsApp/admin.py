from django.contrib import admin
from .models import Question, Answer, OnlineExam

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(OnlineExam)