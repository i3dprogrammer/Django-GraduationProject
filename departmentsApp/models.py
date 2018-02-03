from django.db import models
from django.db.models import Count

class Group(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name

class Department(models.Model):
    prequel = models.OneToOneField(Group, on_delete=models.CASCADE)
    year = models.IntegerField()
    sequels = models.ManyToManyField(Group, related_name="group_sequels")

    def __str__(self):
        return "On {0} year - from {1} to {2} departments".format(self.year, self.prequel, self.sequels.count())