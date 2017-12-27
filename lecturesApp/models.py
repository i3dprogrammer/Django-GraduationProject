from django.db import models
from sessionManagerApp.models import Session

class Lecture(models.Model):
    session = models.ForeignKey(Session)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='lectures/%Y/%m/%d/%H/%M/')

    def __str__(self):
        return self.name + " - " + str(self.session)